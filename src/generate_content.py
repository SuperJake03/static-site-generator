import os
from pathlib import Path

from block_markdown import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        trim_line = line.lstrip()
        if trim_line.startswith("# "):
            return trim_line[2:].strip()
    raise ValueError("no title found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        md = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    new_html = template.replace("{{ Title }}", title)
    new_html = new_html.replace("{{ Content }}", html)
    dir_name = os.path.dirname(dest_path)
    if dir_name != "":
        os.makedirs(dir_name, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(new_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    items = os.listdir(dir_path_content)
    for item in items:
        from_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(from_path) and Path(from_path).suffix == ".md":
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
