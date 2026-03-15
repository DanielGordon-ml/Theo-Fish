# Data Module

## Overview
The data module is responsible for loading and preprocessing academic research. It includes functions for reading data from various sources, cleaning and transforming the data, and preparing it for analysis or modeling. 

We will focus on loading data from Arxiv files, which are commonly used in academic research.
We save that data in graph structure using  **Obsidian**, which allows us to easily navigate and analyze the relationships between different concepts and entities in the research papers.

### Arxiv File Types
For Arxiv we should consider the following types of files:
- **PDF**: The most common format for academic papers, which contains the full text and formatting of the paper. We can use libraries like `PyPDF2` or `pdfminer` to extract text and other relevant information from PDF files.
- **HTML**: Some papers may be available in HTML format, which can be parsed using libraries like `BeautifulSoup` to extract relevant information such as titles, abstracts, authors, and publication dates.
We can also use arXiv API to directly access the metadata and abstracts of papers, which can be more efficient than downloading and parsing PDF files.


### Data Storage
- The raw data directory `C:\python_projects\bamf\Theo-Fish\Data`, contains:
    1. CSV file with three columns
        - `paper_name`: the name of the Arxiv file, which typically includes the title of the paper and its unique identifier.
        - `file_path`: the path to the Arxiv file on the local filesystem or a URL if the file is stored online. This allows us to easily access and manage the raw data for further processing.
        - `file_type`: the type of the Arxiv file, such as PDF, HTML, LaTeX source, or other formats. This information is crucial for determining how to process the file and extract relevant information.
    2. A directory containing the actual Arxiv files, organized in a way that allows for easy access and management. This directory structure can be designed to facilitate efficient processing and retrieval of the raw data as needed.
    3. A directory for storing the processed data as a JSON file, before extracting the mathematical concepts and relationships. This allows us to keep a structured representation of the data that can be easily manipulated and analyzed in subsequent steps of the ETL process. Each JSON file can contain the extracted information from a single paper, including metadata, text, and any other relevant details that we want to retain for further analysis.
- The data vault: `C:\python_projects\bamf\Theo-Fish\ETL\data_vault` is where we store the processed data. Each directory is for a specific paper, and each file is either a definition, theorem, lemma, or other mathematical concept extracted from the paper. We also add one file with the relationships between these concepts, which allows us to create a graph structure for analysis and visualization.
- We need to decide whether to use a graph database like Neo4j or stay with a file-based approach using Obsidian. A graph database would allow for more efficient querying and analysis of the relationships between concepts, while a file-based approach may be simpler to implement and manage. 


## Components
1. **Data Loading**: Functions to read Arxiv files (e.g., PDF or HTML) and extract relevant information such as titles, abstracts, authors, and publication dates.
2. **Data Cleaning**: Functions to clean the extracted data by removing duplicates, correcting errors, and handling missing values.
3. **Data Structuring**: Functions to organize the data into a graph structure where nodes represent entities such as definitions, theorems, lemmas, and other mathematical concepts, and edges represent relationships between these entities. Each theorem, lemma, proposition, etc. must also include the proof, which is a crucial part of the mathematical content. This structured format allows for easier analysis and visualization of the relationships between different concepts in the research papers.
4. **Data Enrichment**: Functions to enrich the data by adding 
    - additional context or information, such as related papers, citations, or external resources. This can help to provide a more comprehensive understanding of the research and its connections to other work in the field.
    - Adding missing steps in the proofs, which can help to fill in gaps in the mathematical content and provide a more complete understanding of the concepts being analyzed.
    - Adding examples or applications of the concepts, which can help to illustrate their relevance and usefulness in real-world scenarios.

### Data Loader
The data loader is responsible for reading the Arxiv files (see the following repo https://github.com/timf34/arxiv2md?tab=readme-ov-file ). It should: 
- Extract relevant information from the files. It includes functions to read files, extract text, extract mathematics, and other relevant information from the papers in a Latex format. The extracted information is then stored in a structured format for further processing. 
- Support multiple file types, such as PDF and HTML, and should be able to handle large volumes of data efficiently. 
- Include error handling to manage issues that may arise during the loading process, such as missing files or unsupported formats.
- Designed to be modular and extensible, allowing for easy addition of new file types or extraction methods as needed.
- Optimized for performance, parallel processing, ensuring that it can process large datasets quickly and efficiently.
- Create the first JSON file for each paper, which contains the extracted information in a structured format. This JSON file serves as an intermediate representation of the data that can be easily manipulated and analyzed in subsequent steps of the ETL process.

#### JSON Must Have Structure
```json
{
    "paper_name": "example_paper.pdf",
    "title": "Example Paper Title",
    "authors": ["Author One", "Author Two"],
    "abstract": "This is an example abstract for the paper.",
    "publication_date": "2024-01-01",
    "extracted_text_latex": "This is the full text extracted from the paper in LaTeX format, including mathematical expressions and other relevant information.",
    "extracted_math": [
        {
            "type": "equation",
            "content": "E = mc^2"
        }
    ]
}
```

### Data Cleaner
The data cleaner is responsible for cleaning the extracted data. It should:
- Remove duplicates - ensuring that the same paper is not processed multiple times, which can lead to redundant data and skewed analysis.
- Correct errors - identifying and correcting any errors in the extracted data, such as misspelled words, incorrect formatting, or missing information.
- Handle missing values - implementing strategies to manage missing data, such as imputation or removal, to ensure the integrity of the dataset.
- Ensure that the cleaned data is in a consistent format, making it easier to analyze and visualize.

### Data Structurer
The data structurer is responsible for organizing the cleaned data into a graph structure. It should:
- Create nodes for each entity (e.g., definitions, theorems, lemmas) and edges for the relationships between them.
- Include the proof for each theorem, lemma, proposition, etc., as part of the node data.
- Allow for easy traversal and querying of the graph to facilitate analysis and visualization of the relationships between different concepts.
- Ensure that the graph structure is flexible and can accommodate various types of relationships and entities as needed.

### Data Enricher
The data enricher is responsible for adding additional context or information to the structured data. It should:
- Add related papers, citations, or external resources to provide a more comprehensive understanding of the research and its connections to other work in the field.
- Add missing steps in the proofs to fill in gaps in the mathematical content and provide a more complete understanding of the concepts being analyzed.
- Add examples or applications of the concepts to illustrate their relevance and usefulness in real-world scenarios.
- Ensure that the enriched data is integrated seamlessly into the existing graph structure, allowing for easy access and analysis of the additional information.

