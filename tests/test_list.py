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