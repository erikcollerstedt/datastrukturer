import unittest
from exercises.list import Node, UnorderedList
from exercises.exceptions import EmptyList


class ListTests(unittest.TestCase):
	def test_is_empty(self):
		l = UnorderedList()
		self.assertTrue(l.is_empty())
		l.add(7)
		self.assertFalse(l.is_empty())
		l.add(13)
		self.assertFalse(l.is_empty())

	def test_size(self):
		l = UnorderedList()
		self.assertEqual(l.size(), 0)
		l.add(7)
		self.assertEqual(l.size(), 1)
		l.add(13)
		self.assertEqual(l.size(), 2)

	def test_search(self):
		l = UnorderedList()
		self.assertFalse(l.search(3))
		l.add(2)
		l.add(4)
		self.assertTrue(l.search(2))

	def test_remove(self):
		l = UnorderedList()
		l.add(1)
		l.add(2)
		l.add(3)
		l.add(4)
		l.add(5)
		self.assertTrue(l.remove(3))
		l.remove(4)
		l.remove(1)
		l.remove(5)
		l.remove(2)
		self.assertTrue(l.is_empty())