import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType
from main import *

class TestSplitImageLinkNodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected_nodes = [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ]
        self.assertListEqual(new_nodes, expected_nodes)
    
    def test_split_images_adjacent(self):
        node = TextNode(
            "This is text with ![two](https://i.imgur.com/zjjcJKZ.png) ![images](https://i.imgur.com/3elNhQu.png) side by side.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected_nodes = [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("two", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" ", TextType.TEXT),
                TextNode("images", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" side by side.", TextType.TEXT),
            ]
        self.assertListEqual(new_nodes, expected_nodes)
    
    def test_split_images_no_images(self):
        node = TextNode(
            "This is text with no images in it.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected_nodes = [
                TextNode("This is text with no images in it.", TextType.TEXT),
            ]
        self.assertListEqual(new_nodes, expected_nodes)
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected_nodes = [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ]
        self.assertListEqual(new_nodes, expected_nodes)
    
    def test_split_links_adjacent(self):
        node = TextNode(
            "This is text with [two](https://i.imgur.com/zjjcJKZ.png) [links](https://i.imgur.com/3elNhQu.png) side by side.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected_nodes = [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("two", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" ", TextType.TEXT),
                TextNode("links", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" side by side.", TextType.TEXT),
            ]
        self.assertListEqual(new_nodes, expected_nodes)
    
    def test_split_links_no_links(self):
        node = TextNode(
            "This is text with no links in it.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected_nodes = [
                TextNode("This is text with no links in it.", TextType.TEXT),
            ]
        self.assertListEqual(new_nodes, expected_nodes)