from binary_search_tree import BST
#from binarySearchTree import BinarySearchTree
import unittest


class BSTTestCase(unittest.TestCase):
    def test_bstTest(self):
        bst = BST()
        
        #Test insert and size
        bst.insert(10)
        self.assertEqual (bst.size(), 1)
        
        bst.insert(5)
        self.assertEqual (bst.size(), 2)
        
        bst.insert(30)
        self.assertEqual (bst.size(), 3)
        
        bst.insert(35)
        self.assertEqual(bst.size(), 4)
        
        self.assertEqual(bst.search_iterative(35), 35)
        self.assertEqual(bst.search(10), 10)
        
        
        self.assertListEqual(bst.inorder_walk(),[5, 10, 30, 35] )
        self.assertListEqual(bst.preorder_walk(),[10, 5, 30, 35] )
        self.assertListEqual(bst.postorder_walk(),[5, 35, 30, 10] )
        
        
        
          
        
        
if __name__== "__main__":
    unittest.main()