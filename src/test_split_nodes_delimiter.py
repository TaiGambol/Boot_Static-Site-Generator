import unittest
from htmlnode import HTMLNode
from textnode import TextNode, TextType
from main import *

class TestSplitNodes(unittest.TestCase):
    def test_no_delimiter(self):
        input_nodes = [TextNode("This text has no delimiters in it.", TextType.TEXT)]
        split_nodes = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        
        expected_nodes = [
            TextNode("This text has no delimiters in it.", TextType.TEXT),
        ]
        self.assertEqual(split_nodes, expected_nodes)
    

    def test_one_pair_delimiters(self):
        input_nodes = [TextNode("This text has **one** pair of delimiters in it.", TextType.TEXT)]
        split_nodes = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        
        expected_nodes = [
            TextNode("This text has ", TextType.TEXT),
            TextNode("one", TextType.BOLD),
            TextNode(" pair of delimiters in it.", TextType.TEXT),
        ]
        self.assertEqual(split_nodes, expected_nodes)
    
    def test_two_pair_delimiters(self):
        input_nodes = [TextNode("This text has _two_ pairs of _delimiters_ in it.", TextType.TEXT)]
        split_nodes = split_nodes_delimiter(input_nodes, "_", TextType.ITALIC)
        
        expected_nodes = [
            TextNode("This text has ", TextType.TEXT),
            TextNode("two", TextType.ITALIC),
            TextNode(" pairs of ", TextType.TEXT),
            TextNode("delimiters", TextType.ITALIC),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(split_nodes, expected_nodes)
    
    def test_invalid_delimiters(self):
        input_nodes = [TextNode("This text has **invalid delimiters in it.", TextType.TEXT)]
        with self.assertRaises(Exception):
            split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        

    def test_multiple_inputs(self):
        input_nodes = [
            TextNode("This text has no delimiters in it.", TextType.TEXT),
            TextNode("This text has `one pair of delimiters` in it.", TextType.TEXT),
            TextNode("This text isn't a TextType.TEXT node, so should be ignored.", TextType.CODE),
        ]
        split_nodes = split_nodes_delimiter(input_nodes, "`", TextType.CODE)
        expected_nodes = [
            TextNode("This text has no delimiters in it.", TextType.TEXT),
            TextNode("This text has ", TextType.TEXT),
            TextNode("one pair of delimiters", TextType.CODE),
            TextNode(" in it.", TextType.TEXT),
            TextNode("This text isn't a TextType.TEXT node, so should be ignored.", TextType.CODE),
        ]
        self.assertEqual(split_nodes, expected_nodes)