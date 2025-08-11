from textnode import TextNode
from textnode import TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    tester = HTMLNode(tag="test", value="second test", children=["third test", "fourth test"], props = {"fifth": "test"})
    print(tester)

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("Invalid text type")
    if text_node.text_type == TextType.TEXT:
        leaf_node = LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        leaf_node = LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        leaf_node = LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        leaf_node = LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        leaf_node = LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        leaf_node = LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
    return leaf_node
    

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        delim_count = node.text.count(delimiter)
        if delim_count % 2 == 1:
            raise Exception("Invalid Markdown syntax")

        split_text = node.text.split(delimiter)
        for idx, text in enumerate(split_text):
            if idx % 2 == 1:
                new_node = TextNode(text, text_type)
                new_nodes.append(new_node)
            else:
                new_node = TextNode(text, TextType.TEXT)
                new_nodes.append(new_node)

    return new_nodes

main()
