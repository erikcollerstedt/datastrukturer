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

	def test_append(self):
		l = UnorderedList()
		l.add(1)
		l.add(2)
		l.append(3)
		self.assertEqual(l.head.next.next.data, 3)

	def test_insert(self):
		l = UnorderedList()
		self.assertTrue(l.insert(0, 4))
		l.add(5)
		l.add(3)
		self.assertTrue(l.insert(2, 5))
		self.assertTrue(l.insert(0, 8))
		self.assertTrue(l.search(8))

	def test_index(self):
		l = UnorderedList()
		l.add(3)
		l.add(4)
		self.assertEqual(l.index(3), 0)

	def test_index_of_empty_list(self):
		l = UnorderedList()
		self.assertRaises(EmptyList, l.index, 1)

	def test_index_not_existing(self):
		l = UnorderedList()
		l.add(3)
		self.assertFalse(l.index(4))

	def test_pop(self):
		l = UnorderedList()
		l.add(1)
		l.add(2)
		l.add(3)
		l.add(4)
		self.assertEqual(l.pop(1), 3)
		self.assertEqual(l.pop(1), 2)

	def test_pop_no_position(self):
		l = UnorderedList()
		l.add(4)
		l.add(5)
		l.add(6)
		l.add(7)
		self.assertEqual(l.pop(), 4)
		self.assertEqual(l.pop(), 5)
		self.assertEqual(l.pop(), 6)
		self.assertEqual(l.pop(), 7)


	def test_pop_one_item(self):
		l = UnorderedList()
		l.add(2)
		l.add(5)
		l.add(4)
		self.assertEqual(l.pop(2), 2)
		self.assertEqual(l.pop(0), 4)

	def test_pop_empty_list(self):
		l = UnorderedList()
		self.assertRaises(EmptyList, l.pop)

	def test_pop_non_position(self):
		l = UnorderedList()
		l.add(2)
		self.assertRaises(IndexError, l.pop, 3)
