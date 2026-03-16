"""
@file test_obsidian_exporter.py
@description Tests for obsidian_exporter.py: vault export with staging,
field preservation, review queue, and manifest output.
"""

import pytest
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

from graph_builder.models.claim import ClaimNode
from graph_builder.models.concept import ConceptNode
from graph_builder.models.edges import (
    ClaimEdge,
    ConceptEdge,
    CouplingEdge,
    SourcedFromEdge,
)
from graph_builder.models.provenance import ProvenanceNode
from graph_builder.models.source import SourceNode
from graph_builder.vault.obsidian_exporter import export_vault

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

ARXIV_ID = "1904.07272"
SANITIZED_ID = "1904-07272"


@pytest.fixture()
def concept() -> ConceptNode:
    """A canonical concept node."""
    return ConceptNode(
        name="Markov Decision Process",
        semantic_type="mathematical_object",
        canonical_definition="A tuple (S, A, P, R, gamma).",
        status="canonical",
    )


@pytest.fixture()
def review_concept() -> ConceptNode:
    """A concept flagged for human review."""
    return ConceptNode(
        name="Ambiguous Object",
        semantic_type="mathematical_object",
        canonical_definition="Needs human review.",
        status="review_needed",
    )


@pytest.fixture()
def claim(concept: ConceptNode) -> ClaimNode:
    """A theorem claim linked to the concept fixture."""
    return ClaimNode(
        source_paper_slug=SANITIZED_ID,
        label="Theorem 1.1",
        claim_type="theorem",
        statement="All rewards are bounded.",
        status="unverified",
    )


@pytest.fixture()
def review_claim() -> ClaimNode:
    """A claim flagged for human review."""
    return ClaimNode(
        source_paper_slug=SANITIZED_ID,
        label="Lemma 2.2",
        claim_type="lemma",
        statement="Unclear statement.",
        status="review_needed",
    )


@pytest.fixture()
def source() -> SourceNode:
    """A source node for the fixture paper."""
    return SourceNode(
        arxiv_id=ARXIV_ID,
        title="Intro MAB",
        authors=["Slivkins, A."],
        date_published="2019-04-15",
    )


@pytest.fixture()
def provenance(concept: ConceptNode) -> ProvenanceNode:
    """A provenance record linking concept to the source."""
    return ProvenanceNode(
        concept_slug=concept.slug,
        source_arxiv_id=ARXIV_ID,
        formulation="(S, A, P, R, γ)",
        section="Ch. 1",
        extraction_confidence=0.95,
    )


def _make_reader(
    concepts: list[ConceptNode],
    claims: list[ClaimNode],
    sources: list[SourceNode],
    concept_edges: list[ConceptEdge] | None = None,
    claim_edges: list[ClaimEdge] | None = None,
    coupling_edges: list[CouplingEdge] | None = None,
    sourced_from: list[SourcedFromEdge] | None = None,
    provenances: list[ProvenanceNode] | None = None,
) -> MagicMock:
    """Build a mock GraphReader returning the provided fixture data."""
    reader = MagicMock()
    reader.get_all_concepts = AsyncMock(return_value=concepts)
    reader.get_all_claims = AsyncMock(return_value=claims)
    reader.get_all_sources = AsyncMock(return_value=sources)
    reader.get_all_concept_edges = AsyncMock(return_value=concept_edges or [])
    reader.get_all_claim_edges = AsyncMock(return_value=claim_edges or [])
    reader.get_all_coupling_edges = AsyncMock(return_value=coupling_edges or [])
    reader.get_all_sourced_from_edges = AsyncMock(return_value=sourced_from or [])
    reader.get_all_provenances = AsyncMock(return_value=provenances or [])
    return reader


def _make_neo4j_client() -> MagicMock:
    """Return a no-op mock Neo4jClient."""
    return MagicMock()


# ---------------------------------------------------------------------------
# Folder structure
# ---------------------------------------------------------------------------


class TestFolderStructure:
    """It should create correct folder structure."""

    @pytest.mark.asyncio
    async def test_it_should_create_required_directories(
        self, tmp_path, concept, source, claim
    ):
        """export_vault creates concepts/, claims/{type}/, sources/, _review/, _meta/."""
        reader = _make_reader([concept], [claim], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        assert (tmp_path / "concepts").is_dir()
        assert (tmp_path / "claims" / "theorems").is_dir()
        assert (tmp_path / "sources").is_dir()
        assert (tmp_path / "_review").is_dir()
        assert (tmp_path / "_meta").is_dir()

    @pytest.mark.asyncio
    async def test_it_should_create_review_subdirs(
        self, tmp_path, review_concept, source, review_claim
    ):
        """_review/concepts/ and _review/claims/ are created for flagged items."""
        reader = _make_reader([review_concept], [review_claim], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        assert (tmp_path / "_review" / "concepts").is_dir()
        assert (tmp_path / "_review" / "claims").is_dir()


# ---------------------------------------------------------------------------
# Concept file writing
# ---------------------------------------------------------------------------


class TestConceptFileWriting:
    """It should write concept files to the correct location."""

    @pytest.mark.asyncio
    async def test_it_should_write_concept_to_slug_md(self, tmp_path, concept, source):
        """concepts/{slug}.md is written for each concept."""
        reader = _make_reader([concept], [], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        expected = tmp_path / "concepts" / f"{concept.slug}.md"
        assert expected.exists()

    @pytest.mark.asyncio
    async def test_it_should_include_frontmatter_in_concept_file(
        self, tmp_path, concept, source
    ):
        """The concept file contains YAML frontmatter delimiters and slug key."""
        reader = _make_reader([concept], [], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        content = (tmp_path / "concepts" / f"{concept.slug}.md").read_text()
        assert content.startswith("---\n")
        assert "slug:" in content
        assert "---" in content[4:]

    @pytest.mark.asyncio
    async def test_it_should_include_body_in_concept_file(
        self, tmp_path, concept, source
    ):
        """The concept body with heading is present below the frontmatter."""
        reader = _make_reader([concept], [], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        content = (tmp_path / "concepts" / f"{concept.slug}.md").read_text()
        assert f"# {concept.name}" in content


# ---------------------------------------------------------------------------
# Claim file writing
# ---------------------------------------------------------------------------


class TestClaimFileWriting:
    """It should write claim files to claims/{claim_type}/{paper-slug}--{claim-slug}.md."""

    @pytest.mark.asyncio
    async def test_it_should_write_claim_under_type_subfolder(
        self, tmp_path, claim, source
    ):
        """Theorem claim lands in claims/theorems/."""
        reader = _make_reader([], [claim], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        claims_dir = tmp_path / "claims" / "theorems"
        files = list(claims_dir.glob("*.md"))
        assert len(files) == 1

    @pytest.mark.asyncio
    async def test_it_should_name_claim_file_paper_slug_claim_slug(
        self, tmp_path, claim, source
    ):
        """Claim filename follows {paper-slug}--{claim-slug}.md convention."""
        reader = _make_reader([], [claim], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        expected = (
            tmp_path / "claims" / "theorems" / f"{claim.slug}.md"
        )
        assert expected.exists()

    @pytest.mark.asyncio
    async def test_it_should_include_frontmatter_in_claim_file(
        self, tmp_path, claim, source
    ):
        """Claim file contains YAML frontmatter with claim_type key."""
        reader = _make_reader([], [claim], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        path = tmp_path / "claims" / "theorems" / f"{claim.slug}.md"
        content = path.read_text()
        assert "claim_type:" in content


# ---------------------------------------------------------------------------
# Source file writing
# ---------------------------------------------------------------------------


class TestSourceFileWriting:
    """It should write source files to sources/{arxiv-id}.md."""

    @pytest.mark.asyncio
    async def test_it_should_write_source_to_arxiv_id_md(self, tmp_path, source):
        """sources/{arxiv_id}.md is created for each source."""
        reader = _make_reader([], [], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        expected = tmp_path / "sources" / f"{source.arxiv_id}.md"
        assert expected.exists()

    @pytest.mark.asyncio
    async def test_it_should_include_arxiv_id_in_source_frontmatter(
        self, tmp_path, source
    ):
        """Source file frontmatter contains the arxiv_id."""
        reader = _make_reader([], [], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        content = (tmp_path / "sources" / f"{source.arxiv_id}.md").read_text()
        assert source.arxiv_id in content


# ---------------------------------------------------------------------------
# Staging + atomic move
# ---------------------------------------------------------------------------


class TestStagingAtomicMove:
    """It should write to staging dir first, then move atomically."""

    @pytest.mark.asyncio
    async def test_it_should_not_leave_staging_dir_after_export(
        self, tmp_path, concept, source
    ):
        """The .staging directory is cleaned up after export completes."""
        reader = _make_reader([concept], [], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        staging = tmp_path / ".staging"
        assert not staging.exists()

    @pytest.mark.asyncio
    async def test_it_should_produce_final_files_after_staging_move(
        self, tmp_path, concept, source
    ):
        """Final concept file is present and staging is absent after export."""
        reader = _make_reader([concept], [], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        final = tmp_path / "concepts" / f"{concept.slug}.md"
        assert final.exists()
        assert not (tmp_path / ".staging").exists()


# ---------------------------------------------------------------------------
# Human-owned field preservation
# ---------------------------------------------------------------------------


class TestHumanFieldPreservation:
    """It should preserve human-owned fields on re-export."""

    @pytest.mark.asyncio
    async def test_it_should_preserve_human_notes_on_concept_re_export(
        self, tmp_path, concept, source
    ):
        """human_notes written by a human survives a second export."""
        reader = _make_reader([concept], [], [source])
        client = _make_neo4j_client()

        # First export
        await export_vault(tmp_path, reader, client)

        # Simulate human edit
        concept_file = tmp_path / "concepts" / f"{concept.slug}.md"
        content = concept_file.read_text()
        content = content.replace("human_notes: ''", "human_notes: 'My note'")
        content = content.replace('human_notes: ""', 'human_notes: "My note"')
        concept_file.write_text(content)

        # Second export
        await export_vault(tmp_path, reader, client)

        updated = concept_file.read_text()
        assert "My note" in updated

    @pytest.mark.asyncio
    async def test_it_should_preserve_canonical_definition_on_re_export(
        self, tmp_path, concept, source
    ):
        """canonical_definition human edits survive re-export."""
        reader = _make_reader([concept], [], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        concept_file = tmp_path / "concepts" / f"{concept.slug}.md"
        content = concept_file.read_text()
        new_def = "Human-refined definition."
        original_def = concept.canonical_definition
        content = content.replace(original_def, new_def)
        concept_file.write_text(content)

        await export_vault(tmp_path, reader, client)

        updated = concept_file.read_text()
        assert new_def in updated

    @pytest.mark.asyncio
    async def test_it_should_preserve_claim_status_on_re_export(
        self, tmp_path, claim, source
    ):
        """A human-set status on a claim file is kept on re-export."""
        reader = _make_reader([], [claim], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        claim_file = tmp_path / "claims" / "theorems" / f"{claim.slug}.md"
        content = claim_file.read_text()
        content = content.replace(
            f"status: {claim.status}", "status: verified"
        )
        claim_file.write_text(content)

        await export_vault(tmp_path, reader, client)

        updated = claim_file.read_text()
        assert "status: verified" in updated


# ---------------------------------------------------------------------------
# Manifest output
# ---------------------------------------------------------------------------


class TestManifestOutput:
    """It should write export-manifest.json with file counts."""

    @pytest.mark.asyncio
    async def test_it_should_write_manifest_json(self, tmp_path, concept, source, claim):
        """export-manifest.json is created in _meta/ after export."""
        reader = _make_reader([concept], [claim], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        manifest_path = tmp_path / "_meta" / "export-manifest.json"
        assert manifest_path.exists()

    @pytest.mark.asyncio
    async def test_it_should_include_concept_count_in_manifest(
        self, tmp_path, concept, source
    ):
        """Manifest contains the number of exported concept files."""
        reader = _make_reader([concept], [], [source])
        client = _make_neo4j_client()

        result = await export_vault(tmp_path, reader, client)

        assert result["concepts"] == 1

    @pytest.mark.asyncio
    async def test_it_should_include_claim_count_in_manifest(
        self, tmp_path, claim, source
    ):
        """Manifest contains the number of exported claim files."""
        reader = _make_reader([], [claim], [source])
        client = _make_neo4j_client()

        result = await export_vault(tmp_path, reader, client)

        assert result["claims"] == 1

    @pytest.mark.asyncio
    async def test_it_should_include_source_count_in_manifest(self, tmp_path, source):
        """Manifest contains the number of exported source files."""
        reader = _make_reader([], [], [source])
        client = _make_neo4j_client()

        result = await export_vault(tmp_path, reader, client)

        assert result["sources"] == 1


# ---------------------------------------------------------------------------
# Review queue
# ---------------------------------------------------------------------------


class TestReviewQueue:
    """It should populate _review/ for status: review_needed items."""

    @pytest.mark.asyncio
    async def test_it_should_write_review_needed_concept_to_review_dir(
        self, tmp_path, review_concept, source
    ):
        """review_needed concepts appear under _review/concepts/."""
        reader = _make_reader([review_concept], [], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        review_dir = tmp_path / "_review" / "concepts"
        files = list(review_dir.glob("*.md"))
        assert len(files) == 1
        assert files[0].name == f"{review_concept.slug}.md"

    @pytest.mark.asyncio
    async def test_it_should_also_write_review_concept_to_main_concepts_dir(
        self, tmp_path, review_concept, source
    ):
        """review_needed concepts appear in both concepts/ and _review/concepts/."""
        reader = _make_reader([review_concept], [], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        main_file = tmp_path / "concepts" / f"{review_concept.slug}.md"
        review_file = tmp_path / "_review" / "concepts" / f"{review_concept.slug}.md"
        assert main_file.exists()
        assert review_file.exists()

    @pytest.mark.asyncio
    async def test_it_should_write_review_needed_claim_to_review_dir(
        self, tmp_path, review_claim, source
    ):
        """review_needed claims appear under _review/claims/."""
        reader = _make_reader([], [review_claim], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        review_dir = tmp_path / "_review" / "claims"
        files = list(review_dir.glob("*.md"))
        assert len(files) == 1

    @pytest.mark.asyncio
    async def test_it_should_not_place_canonical_concepts_in_review_dir(
        self, tmp_path, concept, source
    ):
        """canonical status concepts do not appear in _review/."""
        reader = _make_reader([concept], [], [source])
        client = _make_neo4j_client()

        await export_vault(tmp_path, reader, client)

        review_dir = tmp_path / "_review" / "concepts"
        files = list(review_dir.glob("*.md")) if review_dir.exists() else []
        assert len(files) == 0
