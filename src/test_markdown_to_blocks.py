import unittest
from inline_markdown import *
from block_markdown import *


class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        expected = [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]

        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, expected)


    def test_markdown_empty_blocks(self):
        md = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        expected = [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]

        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, expected)

    def test_markdown_empty_string(self):
        md = ""
        expected = []

        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, expected)

    def test_markdown_ten_newlines(self):
        md = """
This is **bolded** paragraph










This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        expected = [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]

        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, expected)

    def test_markdown_whitespace_between_newlines(self):
        md = """
This is **bolded** paragraph

  

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        expected = [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]

        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, expected)

    def test_markdown_single_line(self):
        md = """
This is **bolded** text. This is text with _italic_ text and `code` here. This is more text.
"""
        expected = [
                "This is **bolded** text. This is text with _italic_ text and `code` here. This is more text.",
            ]

        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, expected)

