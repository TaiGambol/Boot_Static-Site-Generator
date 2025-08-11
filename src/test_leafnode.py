import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_href(self):
        node = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_plain(self):
        node = LeafNode(None, "I'm just some text man")
        self.assertEqual(node.to_html(), "I'm just some text man")

    def test_leaf_to_html_value_error(self):
        node = LeafNode(None, None)
        with self.assertRaises(ValueError):
            node.to_html()

    #def test_leaf_to_html_wtf_value(self):
    #    node = LeafNode(None, {"I'm absolutely": "not supposed to be here"})
    #    self.assertNot