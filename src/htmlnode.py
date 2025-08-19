from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""
        propstring = ""
        for i in self.props:
            propstring = propstring + " " + i + "=\"" + self.props[i] + "\""
        return propstring
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        void_elements = {"img", "hr", "br", "input", "meta", "link"}
        if self.tag in void_elements:
            return f"<{self.tag}{self.props_to_html()}/>"
        if self.value is None:
            print(f"Error, LeafNode missing value. Tag = {self.tag}, props = {self.props}")
            raise ValueError
        if self.tag == None:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    
    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag")
        if self.children is None:
            raise ValueError("No child nodes")
        retString = f"<{self.tag}{self.props_to_html()}>"
        for i in self.children:
            retString = retString + i.to_html()
        retString = retString + f"</{self.tag}>"
        return retString
    
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