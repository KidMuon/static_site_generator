import unittest

from markdown_to_htmlnode import *

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_heading_unordered(self):
        document = """ ### Heading text \n\n* Quick list \n* Quick list2"""
        html = markdown_to_htmlnode(document).to_html()
        self.assertEqual('<div><h3>Heading text</h3><ul><li>Quick list </li><li>Quick list2</li></ul></div>', html)


if __name__ == '__main__':
    unittest.main()