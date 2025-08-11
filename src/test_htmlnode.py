import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props1(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank",})
        expected_string = ' href="https://google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_string)

    def test_props2(self):
        node = HTMLNode(props={})
        expected_string = ''
        self.assertEqual(node.props_to_html(), expected_string)

    def test_props3(self):
        node = HTMLNode(props={"class": "container"})
        expected_string = ' class="container"'
        self.assertEqual(node.props_to_html(), expected_string)

    def test_constructor(self):
        node = HTMLNode(tag="test", value="second test", children=["third test", "fourth test"], props = {"fifth": "test"})
        self.assertEqual(node.tag, "test")
        self.assertEqual(node.value, "second test")
        self.assertEqual(node.children, ["third test", "fourth test"])
        self.assertEqual(node.props, {"fifth": "test"})

    def test_constructorEmpty(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()
    
    def test_repr(self):
        node = HTMLNode(tag="test", value="second test", children=["third test", "fourth test"], props = {"fifth": "test"})
        expected_string = "HTMLNode(tag=test, value=second test, children=['third test', 'fourth test'], props={'fifth': 'test'})"
        self.assertEqual(repr(node), expected_string)
