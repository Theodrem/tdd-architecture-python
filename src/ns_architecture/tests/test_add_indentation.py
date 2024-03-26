# coding: utf-8
import unittest
from ns_architecture.utils import add_indentation
 
 
class AddIndentationTestCase(unittest.TestCase):
    def test_add_indentation_completed_one_level_indentation(self):
        expected_result = '    def test():'
        nb_indent = 1
        line = 'def test():'
        resp = add_indentation(nb_indent=nb_indent, line=line)
        self.assertEqual(expected_result, resp)
 
    def test_add_indentation_completed_double_indentation(self):
        expected_result = 'print(3)'
        nb_indent = 2
        line = 'print(3)'
        resp = add_indentation(nb_indent=nb_indent, line=line)
        self.assertEqual(expected_result, resp)
 
