import os
from git import Repo

# ✅ Always clone inside BE/py/repos — not py/py/repos
REPO_DIR = os.path.join(os.getcwd(), "repos")

def clone_repo(url: str):
    os.makedirs(REPO_DIR, exist_ok=True)
    repo_name = url.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(REPO_DIR, repo_name)

    if os.path.exists(repo_path):
        print(f"✅ Repo already exists at {repo_path}")
    else:
        print(f"⏳ Cloning {url}...")
        Repo.clone_from(url, repo_path)
        print(f"✅ Cloned into {repo_path}")
