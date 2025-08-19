import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType
from inline_markdown import *
from block_markdown import *


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.boot.dev)"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

    def test_extract_markdown_images_plural(self):
        matches = extract_markdown_images(
            "This is text with a ![Python logo image](https://i.imgur.com/zjjcJKZ.png) and a ![meme image](https://i.imgur.com/kJFz2dX.jpeg)"
        )
        self.assertListEqual([("Python logo image", "https://i.imgur.com/zjjcJKZ.png"), ("meme image", "https://i.imgur.com/kJFz2dX.jpeg")], matches)

