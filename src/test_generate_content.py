import unittest

from generate import extract_title


class TestGenerate(unittest.TestCase):
    def test_extract_title(self):
        title1 = extract_title("# Tolkien Fan Club")
        self.assertEqual(title1, "Tolkien Fan Club")
        title2 = extract_title("    # Tolkien Fan Club")
        self.assertEqual(title2, "Tolkien Fan Club")
        with self.assertRaises(ValueError):
            extract_title("## Not a main title")


if __name__ == "__main__":
    unittest.main()
