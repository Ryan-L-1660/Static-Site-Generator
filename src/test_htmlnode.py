import unittest
from htmlnode import HTMLNode

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
        
if __name__ == "__main__":
    unittest.main()