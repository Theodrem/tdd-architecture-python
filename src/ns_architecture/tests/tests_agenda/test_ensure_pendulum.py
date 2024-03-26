# coding: utf-8
import pendulum
import unittest
from agenda.file_to_test import ensure_pendulum
 
 
class EnsurePendulumTestCase(unittest.TestCase):
    def test_ensure_pendulum_completed(self):
        expected_result = pendulum.parse("2023-08-19T08:00:00")
        dt = pendulum.parse("2023-08-19T08:00:00")
        resp = ensure_pendulum(dt=dt)
        self.assertEqual(expected_result, resp)
 
