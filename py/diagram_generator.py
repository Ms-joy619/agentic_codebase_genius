import json
import os
from graphviz import Digraph

INPUT_FILE = "parsed_simple.json"
OUTPUT_FILE = "code_structure_diagram"

def generate_diagram(parsed_file, output_file):
    """Builds a function/class relationship diagram from parsed JSON."""
    if not os.path.exists(parsed_file):
        print(f"❌ File not found: {parsed_file}")
        return

    with open(parsed_file, "r", encoding="utf8") as f:
        data = json.load(f)

    dot = Digraph(comment="Code Structure", format="png")
    dot.attr(rankdir="LR")

    for filepath, items in data.items():
        file_node = os.path.basename(filepath)
        dot.node(file_node, file_node, shape="folder", style="filled", fillcolor="#E0E0E0")

        for cls in items.get("classes", []):
            node_name = f"{file_node}.{cls}"
            dot.node(node_name, cls, shape="box", color="lightblue")
            dot.edge(file_node, node_name)

        for func in items.get("functions", []):
            node_name = f"{file_node}.{func}"
            dot.node(node_name, func, shape="ellipse", color="lightgreen")
            dot.edge(file_node, node_name)

    dot.render(output_file, cleanup=True)
    print(f"✅ Diagram generated and saved as {output_file}.png")

if __name__ == "__main__":
    generate_diagram(INPUT_FILE, OUTPUT_FILE)
