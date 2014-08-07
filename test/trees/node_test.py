import unittest

class SimpleAssertion(unittest.TestCase):
  def setUp(self):
    self.result = 5

  def test_true(self):
    self.assertEqual(self.result, 5)
