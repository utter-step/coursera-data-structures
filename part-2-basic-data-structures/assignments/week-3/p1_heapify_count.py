# python3


def default_gt(a, b):
    """Default comparison operator for heap building."""
    return a > b


def get_parent_i(i):
    """Get index for parent in 0-indexed heap."""
    return (i - 1) // 2


def get_left_child_i(i):
    """Get index for left child in 0-indexed heap."""
    return i * 2 + 1


def get_right_child_i(i):
    """Get index for right child in 0-indexed heap."""
    return i * 2 + 2


def sift_up(heap, i, gt):
    """Sift element at index i up the tree."""
    parent_i = get_parent_i(i)

    while parent_i >= 0 and gt(heap[i], heap[parent_i]):
        heap[i], heap[parent_i] = heap[parent_i], heap[i]
        i = parent_i
        parent_i = get_parent_i(i)

    return heap


def sift_down(heap, i, gt, size=None, record=False):
    """Sift element at index i down the tree."""
    if size is None:
        size = len(heap)
    was_swap = True
    swaps = []

    while was_swap:
        was_swap = False
        top_index = i

        left_child_i = get_left_child_i(i)
        if left_child_i < size and gt(heap[left_child_i], heap[top_index]):
            top_index = left_child_i

        right_child_i = get_right_child_i(i)
        if right_child_i < size and gt(heap[right_child_i], heap[top_index]):
            top_index = right_child_i

        if i != top_index and top_index < size:
            was_swap = True

            if record:
                swaps.append((i, top_index))

            heap[i], heap[top_index] = heap[top_index], heap[i]
            i = top_index

    return swaps


def insert(heap, el, gt=default_gt):
    """Insert el to the correct position in heap."""
    heap.append(el)
    sift_up(heap, len(heap) - 1, gt)


def get_top(heap):
    """Get top heap element."""
    return heap[0]


def extract_top(heap, gt=default_gt):
    """Extract top element from heap and restructure heap afterwards."""
    heap[0], heap[-1] = heap[-1], heap[0]
    top_ = heap.pop()

    sift_down(heap, 0, gt)
    return top_


def remove(heap, i, gt=default_gt):
    """Remove element at index i from heap."""
    heap[i] = heap[0]

    sift_up(heap, i, gt)
    extract_top(heap)


def replace(heap, i, new_value, gt=default_gt):
    """Replace element at index i in heap and reorder heap."""
    old = heap[i]
    heap[i] = new_value
    if old < new_value:
        sift_up(heap, i, gt)
    elif old > new_value:
        sift_down(heap, i, gt)


def heapify(array, gt=default_gt):
    """Reorder given array to binary heap."""
    for i in range(len(array) // 2, -1, -1):
        sift_down(array, i, gt)

    return array


def heap_sort(array, gt=default_gt):
    """
    Heap sort given array.

    >>> heap_sort([1, 10, 5, 3])
    [1, 3, 5, 10]

    >>> heap_sort([1])
    [1]

    >>> heap_sort([1, 0])
    [0, 1]

    >>> heap_sort([1, 2, 3], gt=lambda a, b: a < b)
    [3, 2, 1]

    >>> import random
    >>> arr = [random.randrange(0, 10 ** 8) for _ in range(10000)]
    >>> list(sorted(arr)) == heap_sort(arr)
    True
    """
    heapify(array, gt)
    size = len(array)

    for i in range(1, size):
        array[0], array[-i] = array[-i], array[0]
        size -= 1
        sift_down(array, 0, gt, size)

    return array


def get_swaps(array, gt=default_gt):
    """Reorder given array to binary heap and record needed swaps."""
    swaps = []
    for i in range(len(array) // 2, -1, -1):
        swaps.extend(sift_down(array, i, gt, record=True))

    return swaps


if __name__ == '__main__':
    n = input()
    array = list(map(int, input().split()))

    swaps = get_swaps(array, gt=lambda a, b: a < b)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
