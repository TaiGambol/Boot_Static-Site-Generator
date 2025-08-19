import unittest
from main import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_basic(self):
        markdown = """
# This is a title
The rest of this is nonsense
Lalalala delicious nonsense
"""
        expected = "This is a title"
        result = extract_title(markdown)
        self.assertEqual(expected, result)

    def test_extract_title_error(self):
        markdown = """There's no title in this markdown
        It's a bit shit actually
        Woe to the lack of a title"""
        with self.assertRaises(Exception):
            extract_title(markdown)