"""
@file cycle_detector.py
@description Detects cycles in DEPENDS_ON claim edges using iterative DFS.
"""

from graph_builder.models.edges import ClaimEdge

DEPENDS_ON = "depends_on"


def detect_depends_on_cycles(edges: list[ClaimEdge]) -> list[list[str]]:
    """Find all cycles in DEPENDS_ON edges using DFS.

    Builds an adjacency list from edges where edge_type == 'depends_on',
    then runs DFS from every unvisited node. Each discovered cycle is
    reported as an ordered list of slugs (the back-edge node repeated at
    the end is NOT included — the cycle path starts and ends at the same
    conceptual node).

    Returns list of cycle paths (each path is a list of slugs).
    The same cycle may appear multiple times if it has multiple entry points;
    callers should de-duplicate if needed.
    """
    adjacency = _build_adjacency(edges)
    if not adjacency:
        return []
    return _find_all_cycles(adjacency)


def _build_adjacency(edges: list[ClaimEdge]) -> dict[str, list[str]]:
    """Build adjacency map from DEPENDS_ON edges only."""
    graph: dict[str, list[str]] = {}
    for edge in edges:
        if edge.edge_type != DEPENDS_ON:
            continue
        graph.setdefault(edge.source_slug, [])
        graph.setdefault(edge.target_slug, [])
        graph[edge.source_slug].append(edge.target_slug)
    return graph


def _find_all_cycles(graph: dict[str, list[str]]) -> list[list[str]]:
    """Run DFS over all nodes, collecting back-edge cycles."""
    visited: set[str] = set()
    cycles: list[list[str]] = []

    for start in graph:
        if start not in visited:
            _dfs(start, graph, visited, [], set(), cycles)

    return cycles


def _dfs(
    node: str,
    graph: dict[str, list[str]],
    visited: set[str],
    path: list[str],
    path_set: set[str],
    cycles: list[list[str]],
) -> None:
    """Recursive DFS that records a cycle path when a back edge is found."""
    visited.add(node)
    path.append(node)
    path_set.add(node)

    for neighbour in graph.get(node, []):
        if neighbour in path_set:
            cycle_start = path.index(neighbour)
            cycles.append(path[cycle_start:])
        elif neighbour not in visited:
            _dfs(neighbour, graph, visited, path, path_set, cycles)

    path.pop()
    path_set.discard(node)
