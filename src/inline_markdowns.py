import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("invalid Markdown: missing closing delimiter")
        nodes = []
        for i in range(len(parts)):
            if len(parts[i]) == 0:
                continue
            if i % 2 == 0:
                nodes.append(TextNode(parts[i], TextType.PLAIN))
            else:
                nodes.append(TextNode(parts[i], text_type))
        new_nodes.extend(nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
