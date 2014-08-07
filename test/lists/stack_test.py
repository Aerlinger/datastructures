import unittest
from lists.stack.stack import Stack


class StackTest(unittest.TestCase):

  def setUp(self):
    self.stack = Stack()

  def test_push(self):
    self.stack.push(5)

  def test_pop(self):
    self.stack.push(5)
    result = self.stack.pop()
    self.assertEquals(5, result)

  def test_pop_failure(self):
    self.assertRaises(Exception, self.stack.pop)
