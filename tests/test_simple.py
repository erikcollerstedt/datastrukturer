import unittest
from exercises.simple import Stack, Queue
from exercises.exceptions import EmptyStack, EmptyQueue


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

	#def test_size_empty(self):
	#	s = Stack()

	#	self.assertEqual(s.size(), 0)

	def test_pop(self):
		s = Stack()
		s.push(2)
		self.assertEqual(s.pop(), 2)

	def test_peek(self):
		s = Stack()
		s.push(2)
		s.push(4)
		self.assertEqual(s.peek(), 4)

	def test_peek_empty(self):
		s = Stack()

		self.assertRaises(EmptyStack, s.peek)

	def test_pop_empty(self):
		s = Stack()
		self.assertRaises(EmptyStack, s.pop)

class QueueTests(unittest.TestCase):
	def test_is_empty(self):
		s = Queue()
		self.assertTrue(s.is_empty())

		s.enqueue(2)
		self.assertFalse(s.is_empty())

		s.dequeue()
		self.assertTrue(s.is_empty())

	def test_size(self):
		s = Queue()

		s.enqueue(2)
		self.assertEqual(s.size(), 1)

	#def test_size_empty(self):
	#	s = Queue()

	#	self.assertEqual(s.size(), 0)

	def test_dequeue(self):
		s = Queue()
		s.enqueue(2)
		self.assertEqual(s.dequeue(), 2)

	def test_dequeue_empty(self):
		s = Queue()
		self.assertRaises(EmptyQueue, s.dequeue)

