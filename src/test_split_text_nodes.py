import unittest

from textnode import *
from split_text_nodes import *

class TestSplitTextNode(unittest.TestCase):
    
    def test_split_nodes_delimiter1(self):
        node = TextNode("This is text with a `code block` word", text_type=text_type_code)
        new_nodes = split_nodes_delimiter([node], '`', text_type_code)
        result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text)
        ]
        self.assertEqual(new_nodes, result)
    
    def test_split_nodes_delimiter_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold)
            ],
            new_nodes
        )
    
    def test_split_images(self):
        node = TextNode(
            """This is text with an ![image](image.url) and another ![second](image.url2). Split it please.""",
            text_type_text
        )
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "image.url"),
                TextNode(" and another ", text_type_text),
                TextNode("second", text_type_image, "image.url2"),
                TextNode(". Split it please.", text_type_text)
            ],
            split_nodes_image([node])
        )

    def test_split_link(self):
        node = TextNode(
            """This is text with an [link](link.url) and another [second](link.url2). Split it please.""",
            text_type_text
        )
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("link", text_type_link, "link.url"),
                TextNode(" and another ", text_type_text),
                TextNode("second", text_type_link, "link.url2"),
                TextNode(". Split it please.", text_type_text)
            ],
            split_nodes_links([node])
        )

if __name__ == "__main__":
    unittest.main()
