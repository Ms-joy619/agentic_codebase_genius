# BE/jac/repo_mapper.jac
walker repo_mapper {
    can map_repo(string repo_url) -> map_result {
        # call Python clone_repo
        map = py_module("py.clone_repo").clone_repo(repo_url, "/tmp/codegen_repo");
        if not map["ok"] {
            return {"ok": false, "error": map["message"]};
        }
        path = map["path"];
        file_tree = py_module("py.file_tree").build_file_tree(path);
        readme = py_module("py.file_tree").find_readme(path);
        return {"ok": true, "path": path, "file_tree": file_tree, "readme": readme};
    }
}
