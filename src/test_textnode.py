import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a text node", TextType.PLAIN_TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        node2 = TextNode("This is a text node2", TextType.PLAIN_TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode(
            "This is a text node", TextType.ITALIC_TEXT, "https://www.boot.dev"
        )
        node2 = TextNode(
            "This is a text node", TextType.ITALIC_TEXT, "https://www.boot.dev"
        )
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode(
            "This is a text node", TextType.PLAIN_TEXT, "https://www.boot.dev"
        )
        self.assertEqual(
            "TextNode(This is a text node, plain, https://www.boot.dev)", repr(node)
        )

    def test_url(self):
        node = TextNode("This is a link node", TextType.LINK, "https://boot.dev")
        self.assertTrue(node.url is not None)

    def test_url_is_none(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertTrue(node.url is None)


if __name__ == "__main__":
    unittest.main()
