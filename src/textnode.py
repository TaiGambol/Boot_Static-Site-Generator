from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, node):
        if not isinstance(node, TextNode):
            return False
        return self.text == node.text and self.text_type == node.text_type and self.url == node.url
    
    def __repr__(self):
        self_string = "TextNode("
        self_string = self_string + str(self.text) + ", "
        self_string = self_string + str(self.text_type.value) + ", "
        self_string = self_string + str(self.url) + ")"
        return self_string