import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_1(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        node.to_html()
        res = node.to_html()
        true_res = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(res, true_res)

    def test_to_html_2(self):
        node = ParentNode("PP", [
            ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
        ])

        node.to_html()
        res = node.to_html()
        true_res = "<PP><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></PP>"
        self.assertEqual(res, true_res)

if __name__ == '__main__':
    unittest.main()