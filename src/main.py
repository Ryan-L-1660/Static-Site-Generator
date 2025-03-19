from textnode import TextType, TextNode

def main():

    node1 = TextNode("hello", TextType.BOLD)
    node2 = TextNode("hello", TextType.BOLD)
    node3 = TextNode("world", TextType.ITALIC, "https://example.com")
    
    # Test for equality
    print(node1 == node2)  # True, as text and text_type are identical
    print(node1 == node3)  # False, as text and text_type differ
    print(node1 == "not a text node")  # False, other is not a TextNode 
    node4 = TextNode("This is some text", TextType.BOLD)
    print(node4)
    print(TextNode)
    













if __name__ == "__main__":
    main()