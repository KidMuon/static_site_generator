from leafnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node):
        return (self.text_type == other_node.text_type and
                self.text == other_node.text and
                self.url == other_node.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node: TextNode):

    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == text_type_bold:
        return LeafNode('b', text_node.text)
    elif text_node.text_type == text_type_italic:
        return LeafNode('i', text_node.text)
    elif text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode('a', text_node.text, {"href": text_node.url})
    elif text_node.text_type == text_type_image:
        return LeafNode("img", '', {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Cannot convert TextNode of text_type: {text_node.text_type}")


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