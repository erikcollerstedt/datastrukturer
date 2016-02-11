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
    	self.assertEqual(tree.lookup(6).key, 6)

    def test_lookup_left_exists(self):
    	tree = BinarySearchTree(4)
    	tree.insert(2)
    	tree.insert(3)
    	tree.insert(5)
    	tree.insert(7)
    	self.assertEqual(tree.lookup(2).key, 2)

    def test_lookup_right_not_exists(self):
    	tree = BinarySearchTree(3)
    	self.assertEqual(tree.lookup(7), None)

    def test_lookup_left_not_exists(self):
    	tree = BinarySearchTree(3)
    	self.assertEqual(tree.lookup(1).key, None)