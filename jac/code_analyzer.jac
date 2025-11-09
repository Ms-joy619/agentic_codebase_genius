# BE/jac/code_analyzer.jac
walker code_analyzer {
    can build_ccg(string target_path, list files_to_analyze) -> ccg_result {
        graphs = [];
        for f in files_to_analyze {
            g = py_module("py.ccg_builder").build_ccg_from_python_file(f);
            graphs.append(g);
        }
        merged = py_module("py.ccg_builder").merge_graphs(graphs);
        return {"ok": true, "ccg": merged};
    }

    can query_ccg(dict ccg, string query) -> dict {
        return py_module("py.ccg_builder").query_calls(ccg, query);
    }
}
