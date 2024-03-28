import unittest

from block_markdown import *
from leafnode import *
from parentnode import *

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
        This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        * This is a list
        * with items
        """

        blocks = ["This is **bolded** paragraph",
        """This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line""",
        """* This is a list
        * with items"""
        ]

        self.assertListEqual(
            blocks,
            markdown_to_blocks(markdown)
        )

    def test_if_heading_block(self):
        block = "### This is a heading block"
        self.assertEqual(block_to_block_type(block), block_type_heading)

    def test_if_ordered_list_true(self):
        block = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)

    def test_if_ordered_list_false(self):
        block = "1. First\n2. Second\n4. Third"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

    def test_printing_of_ordered_list(self):
        block = "1. First\n2. Second\n3. Third"
        code_res = block_ordered_list_to_html(block)
        accepted_res = ParentNode('ol', [
            LeafNode('li', "First"),
            LeafNode('li', "Second"),
            LeafNode('li', "Third")
        ])
        self.assertEqual(code_res.to_html(), accepted_res.to_html())
    

if __name__ == '__main__':
    unittest.main()