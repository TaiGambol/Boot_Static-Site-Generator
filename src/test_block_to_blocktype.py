import unittest
from blocktype import BlockType
from inline_markdown import *
from block_markdown import *


class TestBlockType(unittest.TestCase):
    def test_code_block(self):
        block = """```
This is a code block.
```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_heading_block(self):
        block = """## This is a heading"""
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_unordered_list(self):
        block = """- This is an unordered list
- This is an item in the list
- And this is another item"""
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        block = """1. This is an ordered list
2. This is the second item in the list
3. And this is the third item"""
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_misordered_list(self):
        block = """1. This is an ordered list
2. This is the second item in the list
4. And this is the fourth item - where'd 3 go?"""
        self.assertNotEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph(self):
        block = """`This is a block with some of the bits of other blocktypes.
1. It's got a bit of an ordered list
2. This is the second item in that list
- It's got unordered list bits
- Like this too
> It's got a quote
> Or two
And it's just kind of a mess really. Should be a paragraph."""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_quote_empty_line(self):
        block = """>This is a quote block
>
>It's got an empty line in the middle for readability
>But that shouldn't matter to the test."""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
