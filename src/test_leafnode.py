import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_1(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        res = node.to_html()
        self.assertEqual(res, '<a href="https://www.google.com">Click me!</a>')


if __name__ == '__main__':
    unittest.main()