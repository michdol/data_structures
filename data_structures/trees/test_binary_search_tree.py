from data_structures.trees.binary_search_tree import build_tree, search


def test_search():
    root = build_tree()
    assert search(root, 3) == 3
    assert search(root, 1) == 1
    assert search(root, 6) == 6
    assert search(root, 7) is None
