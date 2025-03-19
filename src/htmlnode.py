from textnode import TextNode, TextType
# main class function and def __init__
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self): # An error is being raised for some purpose 
        raise NotImplementedError("Haven't implemented this yet")
    

    def props_to_html(self):
        if self.props is None:
            return ""
        
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'

        return props_str


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

