import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    non_empty_blocks = []
    for block in blocks:
        block = block.strip()
        if block != '':
            non_empty_blocks.append(block)

    return non_empty_blocks

def block_to_block_type(block):
    if _block_is_heading(block):
        return block_type_heading
    elif _block_is_code(block):
        return block_type_code
    elif _block_is_quote(block):
        return block_type_quote
    elif _block_is_unordered_list(block):
        return block_type_unordered_list
    elif _block_is_ordered_list(block):
        return block_type_ordered_list
    else:
        return block_type_paragraph

def _block_is_heading(block):
    # Headings start with 1-6 '#'s
    return len(block.lstrip('#')) + 6 >= len(block) and len(block.lstrip('#')) < len(block)

def _block_is_code(block):
    # Code blocks must begin and end with '```'
    return len(block.strip('`')) + 6 == len(block)

def _block_is_quote(block):
    # Quotes start with '>' on each line
    lines = block.split('\n')
    quote = True
    for line in lines:
        if line[0] != '>':
            quote = False
            break
    return quote

def _block_is_unordered_list(block):
    # Unordered list lines all start with '* ' or '- '
    lines = block.split('\n')
    unordered_list = True
    for line in lines:
        if not bool(re.search(r'^[*-]{1} ', line)):
            unordered_list = False
            break
    return unordered_list

def _block_is_ordered_list(block):
    # Unordered list lines all start with '* ' or '- '
    lines = block.split('\n')
    ordered_list = True
    line_number = 1
    for line in lines:
        if not bool(re.search(f'^{line_number}\.', line)):
            ordered_list = False
            break
        line_number += 1
    return ordered_list
