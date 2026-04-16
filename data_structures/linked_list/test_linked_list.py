import pytest
from linked_list.linked_list import LinkedList, Node


def test_ll_initiate():
    ll = LinkedList()

    assert ll.head is None
    assert ll.length == 0


def test_ll_prepend():
    ll = LinkedList()

    ll.prepend(1)

    assert isinstance(ll.head, Node)
    assert ll.length == 1
    node = ll.head
    assert node.data == 1
    assert node.next is None

    ll.prepend(2)

    assert isinstance(ll.head, Node)
    assert ll.length == 2
    assert ll.head.data == 2
    assert ll.head.next is node


def test_ll_append():
    ll = LinkedList()

    ll.append(1)

    assert isinstance(ll.head, Node)
    assert ll.length == 1
    node = ll.head
    assert node.data == 1
    assert node.next is None

    ll.append(2)

    # Assert head stays the same
    assert ll.head is node
    assert ll.length == 2
    next_node = ll.head.next
    assert isinstance(next_node, Node)
    assert next_node.data == 2
    assert next_node.next is None


def test_ll_get_last():
    ll = LinkedList()

    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)

    node = ll.get_last()
    assert isinstance(node, Node)
    assert node.data == 3
    assert node.next is None


def test_ll_remove_first_empty_list():
    ll = LinkedList()

    result = ll.remove_first()
    assert result is None
    assert ll.length == 0
    assert ll.head is None


def test_ll_remove_first_single_node():
    ll = LinkedList()

    ll.append(1)

    result = ll.remove_first()
    assert result == 1
    assert ll.length == 0
    assert ll.head is None


def test_ll_remove_first_two_nodes():
    ll = LinkedList()

    ll.append(1)
    ll.append(2)

    result = ll.remove_first()
    assert result == 1
    assert ll.length == 1
    assert isinstance(ll.head, Node)
    assert ll.head.data == 2


def test_ll_pop_empty_list():
    ll = LinkedList()

    assert ll.pop() is None
    assert ll.length == 0


def test_ll_pop_single_node():
    ll = LinkedList()

    ll.append(1)

    result = ll.pop()
    assert result == 1
    assert ll.length == 0
    assert ll.head is None


def test_ll_pop_two_nodes():
    ll = LinkedList()

    ll.append(1)
    ll.append(2)

    result = ll.pop()
    assert result == 2
    assert ll.length == 1
    assert isinstance(ll.head, Node)


def test_ll_remove_empty_list():
    ll = LinkedList()

    with pytest.raises(ValueError):
        ll.remove(1)

    assert ll.length == 0


def test_ll_remove_not_found_one_node():
    ll = LinkedList()
    ll.append(1)

    with pytest.raises(ValueError):
        ll.remove(4)

    assert ll.length == 1


def test_ll_remove_not_found_three_nodes():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    with pytest.raises(ValueError):
        ll.remove(4)

    assert ll.length == 3


def test_ll_remove_head_single_node():
    ll = LinkedList()
    ll.append(1)

    result = ll.remove(1)

    assert result == 1
    assert ll.length == 0
    assert ll.head is None


def test_ll_remove_head_two_nodes():
    ll = LinkedList()
    ll.append(1)
    ll.append(1)

    result = ll.remove(1)

    assert result == 1
    assert ll.length == 1
    assert isinstance(ll.head, Node)
    assert ll.head.data == 1
    assert ll.head.next is None


def test_ll_remove_second_node_in_three_nodes_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(1)

    result = ll.remove(2)

    assert result == 2
    assert ll.length == 2
    assert isinstance(ll.head, Node)
    assert ll.head.data == 1
    assert isinstance(ll.head.next, Node)
    assert ll.head.next.data == 1


def test_ll_remove_last_node_in_three_nodes_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    result = ll.remove(3)

    assert result == 3
    assert ll.length == 2
    assert isinstance(ll.head, Node)
    assert ll.head.data == 1
    assert isinstance(ll.head.next, Node)
    assert ll.head.next.data == 2


def test_ll_contains_empty_list():
    ll = LinkedList()

    assert ll.contains(1) is False


def test_ll_contains():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert ll.contains(1) is True
    assert ll.contains(2) is True
    assert ll.contains(3) is True
    assert ll.contains(4) is False


def test_ll_peek():
    ll = LinkedList()

    assert ll.peek() is None

    ll.append(1)
    assert ll.peek() == 1


def test_ll_peek_last():
    ll = LinkedList()

    assert ll.peek_last() is None

    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.peek_last() == 3
