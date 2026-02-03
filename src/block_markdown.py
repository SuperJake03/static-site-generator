def markdown_to_blocks(markdown):
    parts = markdown.split("\n\n")
    blocks = []
    for part in parts:
        block = part.strip()
        if len(block) != 0:
            blocks.append(block)
    return blocks
