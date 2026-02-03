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


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue
        nodes = []
        curr_text = old_node.text
        for text, link in images:
            parts = curr_text.split(f"![{text}]({link})", 1)
            if len(parts[0]) != 0:
                nodes.append(TextNode(parts[0], TextType.PLAIN))
            nodes.append(TextNode(text, TextType.IMAGE, link))
            curr_text = parts[1]
        if len(curr_text) != 0:
            nodes.append(TextNode(curr_text, TextType.PLAIN))
        new_nodes.extend(nodes)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if not links:
            new_nodes.append(old_node)
            continue
        nodes = []
        curr_text = old_node.text
        for text, link in links:
            parts = curr_text.split(f"[{text}]({link})", 1)
            if len(parts[0]) != 0:
                nodes.append(TextNode(parts[0], TextType.PLAIN))
            nodes.append(TextNode(text, TextType.LINK, link))
            curr_text = parts[1]
        if len(curr_text) != 0:
            nodes.append(TextNode(curr_text, TextType.PLAIN))
        new_nodes.extend(nodes)
    return new_nodes


def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.PLAIN)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes
