from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        if tag is None:
            raise ValueError("Tag must be provided to ParentNode")
        if children is None:
            raise ValueError("Children must be provided to ParentNode")
        super().__init__(tag, None, children, props) 
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag assigned to ParentNode")
        if self.children is None:
            raise ValueError("No children assigned to ParentNode")
        child_html = ""
        for child in self.children:
            child_html += child.to_html()
        return self._wrap_children_with_tag(child_html)

    def _wrap_children_with_tag(self, child_html):
        start_tag, end_tag = self._make_tags()
        return start_tag + child_html + end_tag