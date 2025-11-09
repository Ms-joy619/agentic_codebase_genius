import os
import networkx as nx
import ast

def build_ccg_from_python_file(path: str):
    """
    Parse a Python file with ast, extract classes, functions, and call relationships.
    """
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        src = fh.read()
    tree = ast.parse(src, filename=path)
    G = nx.DiGraph()

    class FunctionVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node):
            name = f"{os.path.basename(path)}:{node.name}"
            G.add_node(name, type="function", lineno=node.lineno)
            prev = getattr(self, "current", None)
            self.current = name
            self.generic_visit(node)
            self.current = prev

        def visit_ClassDef(self, node):
            cname = f"{os.path.basename(path)}:class:{node.name}"
            G.add_node(cname, type="class", lineno=node.lineno)
            for base in node.bases:
                try:
                    bname = getattr(base, "id", None) or getattr(base, "attr", None)
                    if bname:
                        G.add_edge(cname, f"class:{bname}", type="inherits")
                except Exception:
                    pass
            self.generic_visit(node)

        def visit_Call(self, node):
            func = node.func
            called = None
            if isinstance(func, ast.Name):
                called = func.id
            elif isinstance(func, ast.Attribute):
                called = func.attr
            if called and hasattr(self, "current") and self.current:
                G.add_node(called, type="function_stub")
                G.add_edge(self.current, called, type="calls")
            self.generic_visit(node)

    v = FunctionVisitor()
    v.visit(tree)
    return G

def merge_graphs(graphs):
    G = nx.DiGraph()
    for g in graphs:
        G.update(g)
    return G

def query_calls(G, function_name):
    res = {"callers": [], "callees": []}
    for u, v, data in G.edges(data=True):
        if u == function_name and data.get("type") == "calls":
            res["callees"].append(v)
        if v == function_name and data.get("type") == "calls":
            res["callers"].append(u)
    return res
