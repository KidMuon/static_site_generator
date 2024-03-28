from block_markdown import *

def markdown_to_htmlnode(document):
    blocks = markdown_to_blocks(document)
    block_types = [block_to_block_type(block) for block in blocks]
    block_tup = zip(blocks, block_types)

    block_parents = []
    for block in block_tup:
        if block[1] == block_type_heading:
            block_parents.append(block_heading_to_html(block[0]))
        elif block[1] == block_type_code:
            block_parents.append(block_code_to_html(block[0]))
        elif block[1] == block_type_quote:
            block_parents.append(block_quote_to_html(block[0]))
        elif block[1] == block_type_unordered_list:
            block_parents.append(block_unordered_list_to_html(block[0]))
        elif block[1] == block_type_ordered_list:
            block_parents.append(block_ordered_list_to_html(block[0]))
        else:
            block_parents.append(block_paragraph_to_html(block[0]))

    return ParentNode("div", block_parents)
