import unittest
from exercises.simple import Stack, Queue

class StackTests(unittest.TestCase):
	def test_is_empty(self):
		s = Stack()
		self.assertEqual(s.is_empty(), True)

		s.push(2)
		self.assertEqual(s.is_empty(), False)

		s.pop()
		self.assertEqual(s.is_empty(), True)

	def test_size(self):
		s = Stack()

		s.push(2)
		self.assertEqual(s.size(), 1)

	def test_pop(self):
		pass

	def test_peek(self):
		s = Stack()

		self.assersRaises(EmptyStack, stack.peek)


class QueueTests(unittest.TestCase):
    pass
