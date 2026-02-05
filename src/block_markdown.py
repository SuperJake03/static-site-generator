from enum import Enum

from htmlnode import ParentNode
from inline_markdowns import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    parts = markdown.split("\n\n")
    blocks = []
    for part in parts:
        block = part.strip()
        if len(block) != 0:
            blocks.append(block)
    return blocks


def block_to_block_type(block):
    lines = block.splitlines()
    for num_hashes in range(1, 7):
        prefix = "#" * num_hashes + " "
        if lines[0].startswith(prefix):
            return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    for i in range(len(lines)):
        if not lines[i].startswith(">"):
            break
        if i == len(lines) - 1:
            return BlockType.QUOTE
    for i in range(len(lines)):
        if not lines[i].startswith("- "):
            break
        if i == len(lines) - 1:
            return BlockType.UNORDERED_LIST
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i + 1}. "):
            break
        if i == len(lines) - 1:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children


def paragraph_to_parent(block):
    text = block.replace("\n", " ")
    children = text_to_children(text)
    parent = ParentNode("p", children)
    return parent


def heading_to_parent(block):
    num_hash = block.count("#")
    text = block[num_hash + 1 :]
    children = text_to_children(text)
    parent = ParentNode(f"h{num_hash}", children)
    return parent


def blockquote_to_parent(block):
    text = block.replace("> ", "").replace(">", "").replace("\n", " ")
    children = text_to_children(text)
    paragraph = ParentNode("p", children)
    parent = ParentNode("blockquote", children)
    return parent


def unordered_to_parent(block):
    lines = block.splitlines()
    inner = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        inner.append(ParentNode("li", children))
    parent = ParentNode("ul", inner)
    return parent


def ordered_to_parent(block):
    lines = block.splitlines()
    inner = []
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        inner.append(ParentNode("li", children))
    parent = ParentNode("ol", inner)
    return parent


def code_to_parent(block):
    lines = block.splitlines()
    text = "\n".join(lines[1:-1]) + "\n"
    raw_text_node = TextNode(text, TextType.PLAIN)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    parent = ParentNode("pre", [code])
    return parent


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            block_nodes.append(paragraph_to_parent(block))
        elif block_type == BlockType.HEADING:
            block_nodes.append(heading_to_parent(block))
        elif block_type == BlockType.QUOTE:
            block_nodes.append(blockquote_to_parent(block))
        elif block_type == BlockType.UNORDERED_LIST:
            block_nodes.append(unordered_to_parent(block))
        elif block_type == BlockType.ORDERED_LIST:
            block_nodes.append(ordered_to_parent(block))
        elif block_type == BlockType.CODE:
            block_nodes.append(code_to_parent(block))
    return ParentNode("div", block_nodes)
