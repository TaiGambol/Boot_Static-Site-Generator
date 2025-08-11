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
        if self.value is None:
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