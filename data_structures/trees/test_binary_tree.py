from data_structures.trees.binary_tree import (
    build_a_tree,
    preorder_traversal,
    inorder_traversal,
    postorder_traversal,
    breadth_first_traversal,
)


def test_preorder_traversal():
    root = build_a_tree()
    result = preorder_traversal(root)
    assert result == [1, 2, 4, 5, 3, 6]


def test_inorder_traversal():
    root = build_a_tree()
    result = inorder_traversal(root)
    assert result == [4, 2, 5, 1, 6, 3]


def test_postorder_traversal():
    root = build_a_tree()
    result = postorder_traversal(root)
    assert result == [4, 5, 2, 6, 3, 1]


def test_breadth_first_traversal():
    root = build_a_tree()
    result = breadth_first_traversal(root)
    assert result == [1, 2, 3, 4, 5, 6]
