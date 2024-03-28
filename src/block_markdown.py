import re
from parentnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

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
    # ordered list lines must all start with #.
    # They must start at 1 and increment by 1
    lines = block.split('\n')
    ordered_list = True
    line_number = 1
    for line in lines:
        if not bool(re.search(f'^{line_number}\.', line)):
            ordered_list = False
            break
        line_number += 1
    return ordered_list

def block_paragraph_to_html(markdown_block):
    child_textnodes = []
    for line in markdown_block.split('\n'):
        child_textnodes.extend(text_to_textnodes(line))
    
    child_leafnodes = []
    for child_textnode in child_textnodes:
        child_leafnodes.append(text_node_to_html_node(child_textnode))
    
    return ParentNode("p", child_leafnodes)

def block_heading_to_html(markdown_block):
    heading_level = len(markdown_block) - len(markdown_block.lstrip('#'))
    markdown_block = markdown_block.lstrip("# ")
    child_textnodes = []
    for line in markdown_block.split('\n'):
        child_textnodes.extend(text_to_textnodes(line))

    child_leafnodes = []
    for child_textnode in child_textnodes:
        child_leafnodes.append(text_node_to_html_node(child_textnode))

    return ParentNode(f"h{heading_level}", child_leafnodes)

def block_code_to_html(markdown_block):
    markdown_block = markdown_block.strip("```")
    child_textnodes = []
    for line in markdown_block.split('\n'):
        child_textnodes.extend(text_to_textnodes(line))

    child_leafnodes = []
    for child_textnode in child_textnodes:
        child_leafnodes.append(text_node_to_html_node(child_textnode))
    
    return ParentNode("pre", [ParentNode("code", child_leafnodes)])

def block_quote_to_html(markdown_block):
    child_textnodes = []
    for line in markdown_block.split('\n'):
        line = line.lstrip(">")
        child_textnodes.extend(text_to_textnodes(line))
    
    child_leafnodes = []
    for child_textnode in child_textnodes:
        child_leafnodes.append(text_node_to_html_node(child_textnode))

    return ParentNode("blockquote", child_leafnodes)

def block_unordered_list_to_html(markdown_block):
    child_textnodes_list = []
    for line in markdown_block.split('\n'):
        pattern_to_replace = re.search(r'^[*-]{1} ', line).group(0)
        line = line.replace(pattern_to_replace, '')
        child_textnodes_list.append(text_to_textnodes(line))

    child_leafnodes = []
    for child_textnodes in child_textnodes_list:
        child_leafnodes.append([text_node_to_html_node(textnode) for textnode in child_textnodes])

    wrapped_child_leafnodes = []
    for leafnode in child_leafnodes:
        wrapped_child_leafnodes.append(ParentNode("li", leafnode))

    return ParentNode("ul", wrapped_child_leafnodes)

def block_ordered_list_to_html(markdown_block):
    child_textnodes_list = []
    for line in markdown_block.split('\n'):
        pattern_to_replace = re.search(r'^\d+\. ', line).group(0)
        line = line.replace(pattern_to_replace, '')
        child_textnodes_list.append(text_to_textnodes(line))

    child_leafnodes = []
    for child_textnodes in child_textnodes_list:
        child_leafnodes.append([text_node_to_html_node(textnode) for textnode in child_textnodes])

    wrapped_child_leafnodes = []
    for leafnode in child_leafnodes:
        wrapped_child_leafnodes.append(ParentNode("li", leafnode))

    return ParentNode("ol", wrapped_child_leafnodes)
