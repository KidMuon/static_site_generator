import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "www.boot.dev")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
