from textnode import TextNode, TextType
import re

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

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            if node.text:
                new_nodes.append(node)
            continue
        text = node.text
        imgmkdwn = extract_markdown_images(text)
        if not imgmkdwn:
            if text:
                new_nodes.append(node)
            continue
        while len(imgmkdwn) >= 1:
            cur_img = imgmkdwn[0]
            img_text = cur_img[0]
            img_url = cur_img[1]
            delim = f"![{img_text}]({img_url})"
            before, remainder = text.split(delim, 1)
            new_node_1 = TextNode(before, TextType.TEXT)
            new_node_2 = TextNode(img_text, TextType.IMAGE, img_url)
            text = remainder
            imgmkdwn = extract_markdown_images(text)
            if before:
                new_nodes.append(new_node_1)
            new_nodes.append(new_node_2)
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            if node.text:
                new_nodes.append(node)
            continue
        text = node.text
        lnkmkdwn = extract_markdown_links(text)
        if not lnkmkdwn:
            if text:
                new_nodes.append(node)
            continue
        while len(lnkmkdwn) >= 1:
            cur_lnk = lnkmkdwn[0]
            lnk_text = cur_lnk[0]
            lnk_url = cur_lnk[1]
            delim = f"[{lnk_text}]({lnk_url})"
            before, remainder = text.split(delim, 1)
            new_node_1 = TextNode(before, TextType.TEXT)
            new_node_2 = TextNode(lnk_text, TextType.LINK, lnk_url)
            text = remainder
            lnkmkdwn = extract_markdown_links(text)
            if before:
                new_nodes.append(new_node_1)
            new_nodes.append(new_node_2)
        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))
    return new_nodes

def split_for_code(node):
    return split_nodes_delimiter(node, "`", TextType.CODE)
def split_for_bold(node):
    return split_nodes_delimiter(node, "**", TextType.BOLD)
def split_for_italic(node):
    return split_nodes_delimiter(node, "_", TextType.ITALIC)


def text_to_textnodes(text):
    start_node = TextNode(text, TextType.TEXT)
    node_list = [start_node]
    splitters = [
        split_for_code, 
        split_for_bold, 
        split_for_italic, 
        split_nodes_image, 
        split_nodes_link,
        ]

    for splitter in splitters:
        new_nodes = []
        for node in node_list:
            if node.text_type == TextType.TEXT:
                new_nodes.extend(splitter([node]))
            else:
                new_nodes.append(node)
        node_list = new_nodes
    return node_list