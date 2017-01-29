import random

import pytest

import p1_heapify_count as p1


class TestHeap:
    """Test heap realization."""

    def test_indexing(self):
        """Test heap indexing."""
        assert p1.get_parent_i(5) == 2
        assert p1.get_left_child_i(5) == 11
        assert p1.get_right_child_i(5) == 12

        assert p1.get_parent_i(0) == -1
        assert p1.get_left_child_i(0) == 1
        assert p1.get_right_child_i(0) == 2

    def test_default_gt(self):
        """Test default comparator."""
        assert p1.default_gt(1, 0)
        assert not p1.default_gt(0, 1)
        assert not p1.default_gt(1, 13)
        assert p1.default_gt(13, 0)

    def test_heapify(self):
        """Test heap building from array."""
        array = [1, 12, 4, 3, 15, 17, 7, 12, 14, 14, 14, 15, 3, 13, 7]
        p1.heapify(array)

        assert len(array) == 15
        for i in range(1, len(array)):
            assert array[i] <= array[p1.get_parent_i(i)]

        assert len(array) == 15
        array = [1, 12, 4, 3, 15, 17, 7, 12, 14, 14, 14, 15, 3, 13, 7]
        p1.heapify(array, gt=lambda a, b: a < b)

        for i in range(1, len(array)):
            assert array[i] >= array[p1.get_parent_i(i)]

    def test_insert(self):
        """Test heap insertion."""
        array = [20, 49, 43, 39, 26, 27, 46, 45, 10, 15, 11, 33, 14, 3, 37]
        p1.heapify(array)
        p1.insert(array, 100500)

        assert len(array) == 16
        assert array[0] == 100500
        assert p1.get_top(array) == 100500

        p1.insert(array, 100501)

        assert len(array) == 17
        assert array[0] == 100501
        assert p1.get_top(array) == 100501

        p1.insert(array, 0)

        assert len(array) == 18
        assert array[0] == 100501
        assert p1.get_top(array) == 100501

    def test_extract_top(self):
        """Test extract_top method."""
        array = [33, 2, 46, 8, 49, 48, 13, 1, 13, 20]
        ordered = [1, 2, 8, 13, 13, 20, 33, 46, 48, 49]
        p1.heapify(array)

        size = 10

        while array:
            assert len(array) == size
            top = p1.extract_top(array)

            size -= 1
            assert len(array) == size
            assert top == ordered.pop()

    def test_heap_sort(self):
        """Test heapsort."""
        array = [35, 24, 48, 18, 31, 28, 26, 9, 24, 8, 47, 27, 38, 4, 24]
        p1.heap_sort(array)

        assert len(array) == 15
        assert array == [
            4, 8, 9, 18, 24, 24, 24, 26, 27, 28, 31, 35, 38, 47, 48]

        p1.heap_sort(array, gt=lambda a, b: a < b)
        assert len(array) == 15
        assert array == [
            48, 47, 38, 35, 31, 28, 27, 26, 24, 24, 24, 18, 9, 8, 4]

    def test_heap_sort_few_unique(self):
        """Test heapsort on array with few unique values."""
        array = [5 - i // 5 for i in range(30)]
        p1.heap_sort(array)

        assert len(array) == 30
        assert array == (
            [0] * 5 + [1] * 5 + [2] * 5 + [3] * 5 + [4] * 5 + [5] * 5)

    @pytest.mark.parametrize('size', [10, 100, 1000, 10000])
    def test_heap_sort_random(self, size):
        """Test heapsort on random data (sparse and dense)."""
        arr = [random.randrange(0, size) for _ in range(size)]
        assert list(sorted(arr)) == p1.heap_sort(arr)

        arr = [random.randrange(0, size // 10) for _ in range(size)]
        assert list(sorted(arr)) == p1.heap_sort(arr)

        arr = [random.randrange(0, max(size // 100, 1)) for _ in range(size)]
        assert list(sorted(arr)) == p1.heap_sort(arr)


class TestSolution:
    """Test Problem 1 solution."""

    def test_example_cases(self):
        """Test on example data from problem statement."""
        arr = [5, 4, 3, 2, 1]
        swaps = p1.get_swaps(arr, gt=lambda a, b: a < b)

        assert len(swaps) == 3
        assert swaps == [(1, 4), (0, 1), (1, 3)]

        arr = [1, 2, 3, 4, 5]
        swaps = p1.get_swaps(arr, gt=lambda a, b: a < b)

        assert len(swaps) == 0
        assert swaps == []

    @pytest.mark.parametrize('size', [10, 100, 1000, 10000, 100000])
    def test_random_data(self, size):
        """Test swaps counter on given data."""
        arr = [random.randrange(0, size) for _ in range(size)]
        arr_copy = list(arr)
        swaps = p1.get_swaps(arr_copy, gt=lambda a, b: a < b)

        assert len(swaps) <= 4 * size

        for i, j in swaps:
            arr[i], arr[j] = arr[j], arr[i]

        assert arr_copy == arr
        for i in range(1, len(arr)):
            assert arr[i] >= arr[p1.get_parent_i(i)]
