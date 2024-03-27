# coding: utf-8
import unittest
from ns_architecture.utils import add_break_line_after_lines
 
 
class AddBreakLineAfterLinesTestCase(unittest.TestCase):
    def test_add_break_line_after_lines_completed(self):
        expected_result = ['hello\n', 'world\n']
        content_file = ['hello', 'world']
        resp = add_break_line_after_lines(content_file=content_file)
        self.assertEqual(expected_result, resp)
 
