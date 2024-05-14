from unittest import TestCase, main

from tree import BinaryTree, Node


class BinarySearchTreeTest(TestCase):
    def setUp(self):
        self.bst = BinaryTree()

    def _populate_tree(self, values=None):
        """
        Root: 20
        L--- 10
            L--- 5
            R--- 15
        R--- 30
            L--- 25
            R--- 35
        
        """
        if not values:
            values = [20, 10, 30, 5, 15, 25, 35]
        # Populate the BST with initial nodes
        for value in values:
            self.bst.insert(value)

    def test_insert_empty(self):
        # Test inserting into an empty BST
        self.bst.insert(10)
        self.assertEqual(self.bst.root.data, 10)
        self.assertIsNone(self.bst.root.left)
        self.assertIsNone(self.bst.root.right)

    def test_insert_smaller(self):
        # Test inserting a smaller value
        self.bst.insert(10)
        self.bst.insert(5)
        self.assertEqual(self.bst.root.left.data, 5)
        self.assertIsNone(self.bst.root.left.left)
        self.assertIsNone(self.bst.root.left.right)

    def test_insert_larger(self):
        # Test inserting a larger value
        self.bst.insert(10)
        self.bst.insert(15)
        self.assertEqual(self.bst.root.right.data, 15)
        self.assertIsNone(self.bst.root.right.left)
        self.assertIsNone(self.bst.root.right.right)

    def test_insert_multiple(self):
        # Test inserting multiple values
        values = [10, 5, 3, 8, 15, 12, 20]
        for value in values:
            self.bst.insert(value)

        # Check the structure of the BST
        self.assertEqual(self.bst.root.data, 10)
        self.assertEqual(self.bst.root.left.data, 5)
        self.assertEqual(self.bst.root.right.data, 15)
        self.assertEqual(self.bst.root.left.left.data, 3)
        self.assertEqual(self.bst.root.left.right.data, 8)
        self.assertEqual(self.bst.root.right.left.data, 12)
        self.assertEqual(self.bst.root.right.right.data, 20)

    def test_search_found_root(self):
        self._populate_tree()
        # Test searching for the root node
        node = self.bst.search(20)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 20)

    def test_search_found_leaf(self):
        self._populate_tree()
        # Test searching for a leaf node
        node = self.bst.search(5)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 5)

    def test_search_found_inner_node(self):
        self._populate_tree()
        # Test searching for a non-leaf, non-root node
        node = self.bst.search(30)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 30)

    def test_search_not_found(self):
        self._populate_tree()
        # Test searching for a non-existent value
        node = self.bst.search(40)
        self.assertIsNone(node)

    def test_search_negative(self):
        self._populate_tree()
        # Test searching for a negative value, assuming no negative values were inserted
        node = self.bst.search(-1)
        self.assertIsNone(node)

    def test_search_non_numeric(self):
        # Test searching for a non-numeric value to ensure type safety, assuming only integers are stored
        with self.assertRaises(TypeError):
            self.bst.search('twenty')

    def test_delete_leaf(self):
        self._populate_tree()
        # Test deleting a leaf node
        self.bst.delete(5)
        self.assertIsNone(self.bst.search(5))
        self.assertIsNotNone(self.bst.search(10))

    def test_delete_node_with_one_child(self):
        self._populate_tree([20, 10, 30, 5, 15, 35])
        # Test deleting a node with one child
        self.bst.delete(30)
        self.assertIsNone(self.bst.search(30))
        self.assertEqual(self.bst.root.right.data, 35)

    def test_delete_node_with_two_children(self):
        self._populate_tree()
        # Test deleting a node with two children
        self.bst.delete(20)
        self.assertIsNone(self.bst.search(20))
        self.assertTrue(self.bst.root.data in [10, 30])  # Assuming a replacement strategy (e.g., in-order successor)

    def test_delete_root(self):
        self._populate_tree()
        # Test deleting the root when it has two children
        self.bst.delete(20)
        self.assertIsNone(self.bst.search(20))
        self.assertTrue(self.bst.root.data != 20)

    def test_delete_nonexistent(self):
        self._populate_tree()
        # Test deleting a node that does not exist
        with self.assertRaises(ValueError):
            self.bst.delete(100)  # Assuming delete raises ValueError on not found

    def test_inorder(self):
        self._populate_tree()
        ret = self.bst.inorder()
        self.assertEqual(ret, [5, 10, 15, 20, 25, 30, 35])

    def test_preorder(self):
        self._populate_tree()
        ret = self.bst.preorder()
        self.assertEqual(ret, [20, 10, 5, 15, 30, 25, 35])

    def test_postorder(self):
        self._populate_tree()
        ret = self.bst.postorder()
        self.assertEqual(ret, [5, 15, 10, 25, 35, 30, 20])

    def test_get_leaves(self):
        self._populate_tree([100, 50, 200, 20, 70, 150, 250, 10, 30, 60, 80, 140, 160, 240, 260])
        ret = self.bst.get_leaves()
        self.assertEqual(ret, [10, 30, 60, 80, 140, 160, 240, 260])

    def test_stacked_inorder(self):
        self._populate_tree()
        ret = self.bst.stacked_inorder()
        self.assertEqual(ret, [5, 10, 15, 20, 25, 30, 35])

    def test_breadth_first_traversal(self):
        """
        Root: 100
            L--- 50
                L--- 25
                    L--- 15
                    R--- 35
                R--- 75
                    L--- 65
                    R--- 85
            R--- 150
                L--- 125
                    L--- 115
                    R--- 135
                R--- 175
                    L--- 165
                    R--- 185
        """
        self._populate_tree([100, 50, 150, 25, 75, 125, 175, 15, 35, 65, 85, 115, 135, 165, 185])
        self.bst.print_tree()
        ret = self.bst.bft()
        self.assertEqual(ret, [100, 50, 150, 25, 75, 125, 175, 15, 35, 65, 85, 115, 135, 165, 185])

    def test_max_avg(self):
        self._populate_tree()
        self.bst.root.right.right.right = Node(15)
        self.bst.root.right.right.left = Node(10)
        self.bst.print_tree()
        ret = self.bst.max_avg()
        self.assertEqual(ret, 8)


if __name__ == "__main__":
    main()