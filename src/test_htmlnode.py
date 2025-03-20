import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):  # Changed name here
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):  # Changed name here
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertTrue(' href="https://www.google.com"' in result)
        self.assertTrue(' target="_blank"' in result)
        self.assertEqual(len(result), len(' href="https://www.google.com" target="_blank"'))

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
if __name__ == "__main__":
    unittest.main()

    