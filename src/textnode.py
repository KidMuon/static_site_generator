from leafnode import LeafNode

text_types = {
    "text": "text",
    "bold": "bold",
    "italic": "italic",
    "code": "code",
    "link": "link",
    "image": "image"
}

class TextNode:
    def __init__(self, text, text_type, url):
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

    match text_node.text_type:
        case text_types.get("text"):
            return LeafNode(None, text_node.text)
        case text_types.get("bold"):
            return LeafNode('b', text_node.text)
        case text_types.get("italic"):
            return LeafNode('i', text_node.text)
        case text_types.get("code"):
            return LeafNode("code", text_node.text)
        case text_types.get("link"):
            return LeafNode('a', text_node.text, {"href": text_node.url})
        case text_types.get("image"):
            return LeafNode("img", '', {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Cannot convert TextNode of text_type: {text_node.text_type}")