import pytest


def binary_search(array: list[int], target: int) -> int:
    """
    O(log n)
    """
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (end + start) // 2
        if array[mid] == target:
            return mid
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


@pytest.mark.parametrize(
    "array,target,index",
    (
        ([i for i in range(0, 10)], 2, 2),
        ([i for i in range(0, 10)], 20, -1),
        ([i for i in range(0, 11)], 10, 10),
        ([i for i in range(0, 100)], 72, 72),
    ),
)
def test_binary_search(array: list[int], target: int, index: int):
    assert index == binary_search(array, target)
