# BE/jac/docgenie.jac
walker docgenie {
    can generate_docs(string repo_path, map file_tree, string readme, map ccg_summary) -> result {
        overview = "";
        if readme != "" {
            overview = py_module("py.simple_summarizer").summarize(readme);
        } else {
            overview = "No README found; basic overview generated.";
        }

        api = [];
        for node in keys(ccg_summary) {
            api.append({"name": node, "summary": "Auto-generated summary."});
        }

        diagram_path = py_module("py.diagram_generator").save_ccg_as_png(ccg_summary, repo_path + "/outputs/ccg.png");

        doc_path = py_module("py.doc_generator").generate_markdown(
            project_name = os.path.basename(repo_path),
            overview = overview,
            installation = "See README or setup.py",
            usage = "See README or examples",
            file_tree = file_tree,
            api = api,
            diagrams = [diagram_path],
            outdir = os.path.join(repo_path, "outputs")
        );
        return {"ok": true, "doc_path": doc_path};
    }
}
