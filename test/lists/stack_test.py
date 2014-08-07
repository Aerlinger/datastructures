import unittest
from lists.stack.stack import Stack


class StackTest(unittest.TestCase):

  def setUp(self):
    self.stack = Stack()

  def test_pop(self):
    self.stack.push(5)
    result = self.stack.pop()

    self.assertEquals(5, result)

  def test_pop_failure(self):
    self.assertRaises(Exception, self.stack.pop)

  def test_push_failure(self):
    for i in range(11):
      self.stack.push(i)

    self.assertRaises(Exception, self.stack.push, 5)
    