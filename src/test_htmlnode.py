import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_props_to_html1(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        verify = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(verify, node.props_to_html())

    def test_props_to_html2(self):
        node = HTMLNode()
        verify = ""
        self.assertEqual(verify, node.props_to_html())

    def test_props_to_html3(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_repr1(self):
        node = HTMLNode(
            "p",
            "This is a test node",
            [HTMLNode()],
            {"href": "https://www.google.com", "target": "_blank"},
        )
        self.assertEqual(
            "HTMLNode(p, This is a test node, children: [HTMLNode(None, None, children: None, None)], {'href': 'https://www.google.com', 'target': '_blank'})",
            repr(node),
        )

    def test_repr2(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_repr_leaf(self):
        node = LeafNode(
            "p",
            "What a strange world",
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "LeafNode(p, What a strange world, {'class': 'primary'})",
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
