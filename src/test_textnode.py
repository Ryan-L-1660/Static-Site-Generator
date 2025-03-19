import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_repr(self):
        node = TextNode("text here", TextType.BOLD)
        self.assertEqual(repr(node), "TextNode(text='text here', text_type=TextType.BOLD, url=None)")

    def test_url(self):
        node = TextNode("here for text", TextType.BOLD)

        #check if the url is none 
        self.assertEqual(node.url, None)

        node_with_url = TextNode("here for text", TextType.LINK, "https://example.com")
        self.assertEqual(node_with_url.url, "https://example.com")

        self.assertNotEqual(node, node_with_url)


    def test_different_text_type(self):
        node1 = TextNode("same text", TextType.BOLD)
        node2 = TextNode("same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)
        


if __name__ == "__main__":
    unittest.main()