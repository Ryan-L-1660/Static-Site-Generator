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
    

# leafnode inherits from parent htmlnode
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, children=None, props=props, value=value)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")
        
        # check if tag exists 
        if self.tag is None: 
            return self.value
        
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
    



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)


    def to_html(self):

        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        props_html = self.props_to_html()

        html = f"<{self.tag}{props_html}>"

        for child in self.children:
            html += child.to_html()

        html += f"</{self.tag}>"

        return html
    

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:  
        return LeafNode("code", text_node.text)  
    elif text_node.text_type == TextType.LINK:  
        props = {"href": text_node.url}
        return LeafNode("a", text_node.text, props)
    elif text_node.text_type == TextType.IMAGE:  
        props = {"src": text_node.url, "alt": text_node.text} 
        return LeafNode("img", "", props)
    else:
        raise Exception("Unknown text type")




               

