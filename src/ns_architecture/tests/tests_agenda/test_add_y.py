# coding: utf-8
import unittest
from agenda.file_to_test import add_y
 
 
class AddYTestCase(unittest.TestCase):
    def test_add_y_completed(self):
        expected_result = 6
        x = 3
        y = 3
        resp = add_y(x=x, y=y)
        self.assertEqual(expected_result, resp)
 
