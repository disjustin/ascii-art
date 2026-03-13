import unittest
import sys
from io import StringIO
from print_ascii_text import get_char_lines, FONT

class TestASCIIArt(unittest.TestCase):
    def test_upper_a(self):
        lines = get_char_lines('A', False, 'upper')
        self.assertEqual(lines[0], ' AAA ')
        self.assertEqual(lines[2], 'AAAAA')

    def test_lower_a(self):
        lines = get_char_lines('a', False, 'lower')
        self.assertEqual(lines[2], ' ### ')
        self.assertEqual(lines[6], '     ')

    def test_bold_upper(self):
        lines = get_char_lines('A', True, 'upper')
        self.assertEqual(lines[0], ' ### ')
        self.assertEqual(lines[2], '#####')

    def test_bold_lower(self):
        lines = get_char_lines('a', True, 'lower')
        self.assertEqual(lines[2], ' ### ')
        self.assertEqual(lines[4], '# ## ')

    def test_mixed_case(self):
        # Test 'A' with case='none'
        lines = get_char_lines('A', False, 'none')
        self.assertEqual(lines[0], ' AAA ')

    def test_unknown_char(self):
        lines = get_char_lines('1', False, 'none')
        self.assertEqual(lines, FONT['1'])

if __name__ == '__main__':
    unittest.main()
