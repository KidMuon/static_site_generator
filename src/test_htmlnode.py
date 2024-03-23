import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        string = node.props_to_html()
        self.assertEqual(string, 'href="https://www.google.com" target="_blank"')

    def test_repl_1(self):
        node = HTMLNode("a", "Text Body", None, {"href": "https://www.google.com", "target": "_blank"})
        res = node.__repr__()
        self.assertEqual(res, f"HTMLNode(a, Text Body, None, {node.props_to_html()})")


if __name__ == "__main__":
    unittest.main()
