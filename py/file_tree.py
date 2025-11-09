import os
import json

REPO_PATH = "repos/Hello-World"
OUTPUT_FILE = "repo_tree.json"

def build_file_tree(repo_path):
    tree = {}
    for root, dirs, files in os.walk(repo_path):
        rel_path = os.path.relpath(root, repo_path)
        tree[rel_path] = {
            "dirs": dirs,
            "files": files
        }
    return tree

if __name__ == "__main__":
    if not os.path.exists(REPO_PATH):
        print(f"❌ Repo path not found: {REPO_PATH}")
    else:
        print(f"📁 Building file tree for {REPO_PATH}")
        tree = build_file_tree(REPO_PATH)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(tree, f, indent=4)
        print(f"✅ File tree saved to {OUTPUT_FILE}")
