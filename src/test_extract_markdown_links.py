import unittest

from extract_markdown_links import *


class TestExtractFunctions(unittest.TestCase):
    def test_image_link_extraction(self):
        image_embedded_text = """
        This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)
        and ![another](https://i.imgur.com/dfsdkjfd.png).
        """
        self.assertListEqual(
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("another", "https://i.imgur.com/dfsdkjfd.png")
            ], 
            extract_markdown_images(image_embedded_text)
        )

    def test_link_extraction(self):
        link_embedded_text = """
        This is test with a [link](https://www.example.com)
         and [another](https://www.example.com/another)
        """
        self.assertListEqual(
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another")
            ],
            extract_markdown_links(link_embedded_text)
        )

if __name__ == "__main__":
    unittest.main()