import unittest

from textnode import *
from inline_markdown import *

class TestSplitTextNode(unittest.TestCase):
    
    def test_split_nodes_delimiter1(self):
        node = TextNode("This is text with a `code block` word", text_type=text_type_code)
        new_nodes = split_nodes_delimiter([node], '`', text_type_code)
        result = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text)
        ]
        self.assertListEqual(result, new_nodes)
    
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
    #@unittest.SkipTest
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        self.maxDiff = None
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
            text_to_textnodes(text)
        )

if __name__ == "__main__":
    unittest.main()
