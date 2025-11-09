The Agentic Codebase Genius project automates the process of understanding a software codebase by combining Jac agents and Python helper scripts. Each component performs a specific role in analyzing, visualizing, and documenting any GitHub repository.

Jac Agent Orchestration
The process begins with main.jac, which initializes the main Jac walker (agent). This agent coordinates the entire workflow by triggering other Jac modules such as repo_mapper.jac, code_analyzer.jac, and docgenie.jac. Each Jac walker is responsible for a distinct part of the analysis, allowing the system to operate in a modular and automated way.

Repository Cloning
The repo_mapper.jac agent interacts with the Python script clone_repo.py to clone the target GitHub repository into the local workspace (py/repos). If the repository is already present, it skips the cloning step to avoid unnecessary repetition.

Code Parsing and Structure Analysis
Once the repository has been cloned, the code_analyzer.jac agent uses Python scripts such as parser_tree_sitter.py and file_tree.py to scan all Python files. These scripts rely on Python’s Abstract Syntax Tree (AST) and directory traversal methods to extract important details such as class and function definitions, file structures, and relationships between different components. The results of this analysis are then stored in a structured JSON file called parsed_simple.json.

Graph and Diagram Generation
The data generated from the analysis is passed to the diagram_generator.py script, which uses Graphviz to create a visual diagram (code_structure_diagram.png). This diagram provides a clear representation of how the different files, classes, and functions in the codebase are connected, making it easier to understand the overall structure of the project.

Documentation Generation
The docgenie.jac agent works with doc_generator.py and simple_summarizer.py to produce human-readable documentation. This documentation explains the purpose of each file, summarizes key functions and classes, and outlines how the different parts of the codebase interact.

Output
After the process is complete, the following outputs are produced:

parsed_simple.json – a structured representation of the code analysis

code_structure_diagram.png – a visual diagram showing file and function relationships

Optionally, a generated README or Markdown file summarizing the repository’s structure and behavior
