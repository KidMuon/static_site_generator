from textnode import *
from extract_markdown_links import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []

    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter, maxsplit = 2)
        if len(split_text) == 1:
            node.text_type = text_type_text
            new_nodes.append(node)
            continue
        if len(split_text) != 3:
            # pylint: disable=locally-disabled, broad-exception-raised
            raise Exception(f"""
            No matching {delimiter} found in: '{node.text}'.
            This is invalid markdown syntax
            """)

        if split_text[0] != '':
            new_nodes.append(TextNode(split_text[0], text_type_text))
        new_nodes.append(TextNode(split_text[1], text_type))
        if split_text[2] != '':
            sub_nodes = split_nodes_delimiter(
                [TextNode(split_text[2], node.text_type)],
                delimiter=delimiter,
                text_type=text_type)
            new_nodes.extend(sub_nodes)

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)

        images = extract_markdown_images(node.text)
        temp_image_tag = '![image]!'
        split_text = replace_markdown_images(
            node.text,
            temp_image_tag
            ).split(temp_image_tag)

        #pylint: disable=locally-disabled, consider-using-enumerate
        for image_index in range(len(images)):
            new_nodes.append(
                TextNode(split_text[image_index], text_type_text)
                )
            new_nodes.append(
                TextNode(
                    images[image_index][0],
                    text_type_image,
                    images[image_index][1])
                )
        new_nodes.append(TextNode(split_text[-1], text_type_text))

    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)

        links = extract_markdown_links(node.text)
        temp_link_tag = '![link]!'
        split_text = replace_markdown_links(
            node.text,
            temp_link_tag
            ).split(temp_link_tag)

        #pylint: disable=locally-disabled, consider-using-enumerate
        for link_index in range(len(links)):
            new_nodes.append(
                TextNode(split_text[link_index], text_type_text)
                )
            new_nodes.append(
                TextNode(
                    links[link_index][0],
                    text_type_link,
                    links[link_index][1])
                )
        new_nodes.append(TextNode(split_text[-1], text_type_text))

    return new_nodes
