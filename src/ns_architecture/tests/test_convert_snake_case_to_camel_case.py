# coding: utf-8
import unittest
from ns_architecture.utils import convert_snake_case_to_camel_case
 
 
class ConvertSnakeCaseToCamelCaseTestCase(unittest.TestCase):
    def test_convert_snake_case_to_camel_case_completed(self):
        expected_result = 'TestWithFile'
        file_str = 'test_with_file'
        resp = convert_snake_case_to_camel_case(file_str=file_str)
        self.assertEqual(expected_result, resp)
 
    def test_convert_snake_case_to_camel_case_completed_w_one_word(self):
        expected_result = 'Test'
        file_str = 'test'
        resp = convert_snake_case_to_camel_case(file_str=file_str)
        self.assertEqual(expected_result, resp)
 
