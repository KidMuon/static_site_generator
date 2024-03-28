class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return None
        html_string = ""
        for attr in self.props:
            html_string += f'{attr}="{self.props[attr]}" '
        html_string = html_string.rstrip(" ")
        return html_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"

    def _make_tags(self):
        start_tag = f"<{self.tag}"
        if self.props is not None:
            start_tag += " "
            start_tag += self.props_to_html()
        start_tag += ">"

        end_tag = f"</{self.tag}>"
        return start_tag, end_tag