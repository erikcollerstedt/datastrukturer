import unittest
from exercises.tree import BinarySearchTree


class TreeNodeTests(unittest.TestCase):
	pass

class TreeTests(unittest.TestCase):

    def test_left_insert(self):
    	#test insert right
    	tree = BinarySearchTree(3)
    	tree.insert(5)
    	tree.insert(3)
    	tree.insert(6)
    	self.assertEqual(tree.right.key, 5)

    def test_right_insert(self):
    	#test insert left
    	tree = BinarySearchTree(5)
    	tree.insert(3)
    	tree.insert(2)
    	tree.insert(4)
    	self.assertEqual(tree.left.key, 3)

    def test_lookup_right_exists(self):
    	#test lookup right if key exists 
    	tree = BinarySearchTree(5)
    	tree.insert(2)
    	tree.insert(6)
    	tree.insert(0)
    	tree.insert(3)
    	self.assertEqual(tree.lookup(6)[0].key, 6)

    def test_lookup_left_exists(self):
    	tree = BinarySearchTree(4)
    	tree.insert(2)
    	tree.insert(3)
    	tree.insert(5)
    	tree.insert(7)
    	self.assertEqual(tree.lookup(2)[0].key, 2)

    def test_lookup_right_not_exists(self):
    	tree = BinarySearchTree(3)
    	self.assertEqual(tree.lookup(7)[0], None)

    def test_lookup_left_not_exists(self):
    	tree = BinarySearchTree(3)
    	self.assertEqual(tree.lookup(1)[0], None)

    def test_delete_tree(self):
    	tree = BinarySearchTree(3)
    	self.assertRaises(Exception, tree.delete, 3)

    def test_delete_one_child(self):
    	#tesing delete nodes parent, node has one child (right side)
	    self.t = BinarySearchTree(10)
	    self.t.insert(15)
	    self.t.insert(20)
	    self.t.delete(10)
	    self.assertEqual(self.t.lookup(15)[0].key, 15)
	    self.assertEqual(self.t.lookup(20)[0].key, 20)
	    self.assertIsNone(self.t.lookup(10)[0])


class TreeDeleteTests(unittest.TestCase):
	def setUp(self):
		#        10
		#       /   \
		#     5       15
		#    /       /  \
		#   2      12    20
		#  / \
		# 1   3

		self.t = BinarySearchTree(10)
		self.t.insert(5)
		self.t.insert(2)
		self.t.insert(1)
		self.t.insert(3)
		self.t.insert(15)
		self.t.insert(12)
		self.t.insert(20)

	def test_delete_leaf_left(self):
		self.t.delete(12)
		self.assertIsNone(self.t.lookup(12)[0])
		self.assertEqual(self.t.lookup(15)[0].key, 15)
		self.assertEqual(self.t.lookup(20)[0].key, 20)

	def test_delete_leaf_right(self):
		self.t.delete(20)
		self.assertIsNone(self.t.lookup(20)[0])
		self.assertEqual(self.t.lookup(12)[0].key, 12)
		self.assertEqual(self.t.lookup(15)[0].key, 15)

	def test_delete_one_child(self):
		self.t.delete(5)
		self.assertIsNone(self.t.lookup(5)[0])
		self.assertEqual(self.t.lookup(1)[0].key, 1)
		self.assertEqual(self.t.lookup(2)[0].key, 2)
		self.assertEqual(self.t.lookup(3)[0].key, 3)
		self.assertEqual(self.t.lookup(10)[0].key, 10)

	def test_delete_parent(self):
		self.t.delete(2)
		self.assertIsNone(self.t.lookup(2)[0])
		self.assertEqual(self.t.lookup(5)[0].key, 5)
		self.assertEqual(self.t.lookup(3)[0].key, 3)
		self.assertEqual(self.t.lookup(1)[0].key, 1)

	def test_delete_no_parent(self):
		self.t.delete(10)
		self.assertIsNone(self.t.lookup(10)[0])
		self.assertEqual(self.t.lookup(5)[0].key, 5)

	def test_one_child_no_parent(self):
	#Test for one child and no parent, left side
		self.t.delete(15)
		self.t.delete(12)
		self.t.delete(20)
		self.t.delete(10)
		self.assertEqual(self.t.lookup(5)[0].key, 5)
		self.assertListEqual([x.key for x in self.t.lookup(2)], [2, 5])
		self.assertListEqual([x.key for x in self.t.lookup(1)], [1, 2])
		self.assertListEqual([x.key for x in self.t.lookup(3)], [3, 2])


	def test_traverse(self):
		self.assertEqual([1, 2, 3, 5, 10, 12, 15, 20], [x.key for x in self.t.traverse()])

	def test_str(self):
		self.assertEqual(self.t.__str__(), '1, 2, 3, 5, 10, 12, 15, 20')

