import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
