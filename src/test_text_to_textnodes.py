import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType
from main import *

class TestTextToTextNodes(unittest.TestCase):
    def test_all_the_markdown(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected)
    
    def test_no_markdown(self):
        text = "This is plain text with no markdown at all."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is plain text with no markdown at all.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
    
    def test_adjacent_markdown(self):
        text = "This is text with **bold**_italic_ text, and a grammatical error."
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text, and a grammatical error.", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
    
    def test_overlapping_markdown(self):
        text = "This text has **bolded and _italic_** overlap, which shouldn't work!"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This text has ", TextType.TEXT),
            TextNode("bolded and _italic_", TextType.BOLD),
            TextNode(" overlap, which shouldn't work!", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_no_input(self):
        text = ""
        result = text_to_textnodes(text)
        expected = []
        self.assertEqual(result, expected)