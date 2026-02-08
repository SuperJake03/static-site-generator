import os

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
    raise NotImplementedError
