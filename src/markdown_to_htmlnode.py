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

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == block_type_heading and block_heading_to_html(block).tag == 'h1':
            return block.lstrip('# ')
    # pylint: disable=locally-disabled, broad-exception-raised
    raise Exception('No h1 header found. Page has no title')

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_document = ''
    with open(from_path) as f:
        markdown_document = f.read()

    template_document = ''
    with open(template_path) as f:
        template_document = f.read()

    html_contents = markdown_to_htmlnode(markdown_document)

    html_title = extract_title(markdown_document)

    html_page = template_document.replace('{{ Title }}', html_title).replace('{{ Content }}', html_contents.to_html())

    with open(dest_path, 'w') as f:
        f.write(html_page)

    return None
