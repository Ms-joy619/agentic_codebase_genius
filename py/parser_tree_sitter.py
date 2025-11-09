import ast
import os
import json

REPO_PATH = "repos/Hello-World"
OUTPUT_FILE = "parsed_simple.json"

def parse_file(path):
    with open(path, "r", encoding="utf8", errors="ignore") as f:
        tree = ast.parse(f.read(), filename=path)
    funcs = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    return {"functions": funcs, "classes": classes}

def parse_repo(repo_path):
    data = {}
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                full = os.path.join(root, file)
                data[full] = parse_file(full)
    return data

if __name__ == "__main__":
    if os.path.exists(REPO_PATH):
        parsed = parse_repo(REPO_PATH)
        with open(OUTPUT_FILE, "w", encoding="utf8") as f:
            json.dump(parsed, f, indent=2)
        print("✅ Parsing complete (simple). Saved to", OUTPUT_FILE)
    else:
        print("❌ Repo path not found:", REPO_PATH)
