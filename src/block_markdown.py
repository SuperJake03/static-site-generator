from enum import Enum


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
