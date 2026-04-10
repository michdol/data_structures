import pytest


def merge_sort(array: list[int]) -> list[int]:
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    temp = []
    i, j = 0, 0
    i_end = len(left)
    j_end = len(right)
    while i < i_end and j < j_end:
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    while i < i_end:
        temp.append(left[i])
        i += 1
    while j < j_end:
        temp.append(right[j])
        j += 1
    return temp


@pytest.mark.parametrize(
    "array,expected",
    (
        ([2, 1], [1, 2]),
        (
            [91, 92, 58, 83, 59, 99, 45, 3, 2, 98],
            [2, 3, 45, 58, 59, 83, 91, 92, 98, 99],
        ),
        (
            [39, 98, 80, 27, 23, 97, 86, 2, 60, 21],
            [2, 21, 23, 27, 39, 60, 80, 86, 97, 98],
        ),
        (
            [41, 83, 2, 37, 21, 45, 64, 39, 27, 4, 79, 48, 47, 40, 13],
            [2, 4, 13, 21, 27, 37, 39, 40, 41, 45, 47, 48, 64, 79, 83],
        ),
    ),
)
def test_merge_sort(array, expected):
    result = merge_sort(array)
    assert result == expected, result
