from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("All leaf nodes require a value")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("No value assigned to LeafNode")
        if self.tag is not None:
            return self._wrap_with_tag()
        return self.value

    def _wrap_with_tag(self):
        start_tag, end_tag = self._make_tags()
        return start_tag + self.value + end_tag