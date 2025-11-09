import os
from jinja2 import Template

DOC_TEMPLATE = """
# {{ project_name }}

## Overview
{{ overview }}

## Installation
{{ installation }}

## Usage
{{ usage }}

## File tree
{% macro render_tree(node, level=0) -%}
{{ "  "*level }}- **{{ node.name }}** ({{ node.type }})
{%- for child in node.children %}
{{ render_tree(child, level+1) }}
{%- endfor %}
{%- endmacro %}
{{ render_tree(file_tree) }}

## API Reference
{% for item in api %}
### {{ item.name }}
{{ item.summary }}
{% endfor %}

## Diagrams
{% for img in diagrams %}
![{{ img }}]({{ img }})
{% endfor %}
"""

def generate_markdown(project_name, overview, installation, usage, file_tree, api, diagrams, outdir):
    tpl = Template(DOC_TEMPLATE)
    md = tpl.render(
        project_name=project_name,
        overview=overview,
        installation=installation,
        usage=usage,
        file_tree=file_tree,
        api=api,
        diagrams=diagrams,
    )
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "docs.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(md)
    return path
