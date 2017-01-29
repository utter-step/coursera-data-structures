import random

import pytest

from p2_threads import Heap, thread_priority_greater, schedule_jobs


TEST_PRIORITY_TEST_CASES = (
    ((0, 0), (1, 0), True),
    ((1, 1), (1, 0), False),
    ((0, 10), (1, 0), False),
    ((5, 0), (1, 1), True),
    ((1, 2), (3, 4), True),
    ((4, 3), (2, 1), False),
    ((2, 1), (4, 3), True),
    ((0, 6), (1, 6), True),
    ((3, 6), (1, 6), False),
)

EXAMPLE_INPUTS = (
    (2, (1, 2, 3, 4, 5)),
    (4, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)),
)
EXAMPLE_OUTPUTS = (
    [
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 2),
        (0, 4),
    ],
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (0, 1),
        (1, 1),
        (2, 1),
        (3, 1),
        (0, 2),
        (1, 2),
        (2, 2),
        (3, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
        (0, 4),
        (1, 4),
        (2, 4),
        (3, 4),
    ],
)


class TestHeapClass:
    """Test heap realization."""

    def test_indexing(self):
        """Test heap indexing."""
        assert Heap.get_parent_i(5) == 2
        assert Heap.get_left_child_i(5) == 11
        assert Heap.get_right_child_i(5) == 12

        assert Heap.get_parent_i(0) == -1
        assert Heap.get_left_child_i(0) == 1
        assert Heap.get_right_child_i(0) == 2

    def test_default_gt(self):
        """Test default comparator."""
        assert Heap._default_gt(1, 0) is True
        assert Heap._default_gt(0, 1) is False
        assert Heap._default_gt(1, 13) is False
        assert Heap._default_gt(13, 0) is True

    def test_heapify(self):
        """Test heap building from array."""
        heap = Heap()
        array = [1, 12, 4, 3, 15, 17, 7, 12, 14, 14, 14, 15, 3, 13, 7]
        heap.heapify(array)

        assert heap.size == 15
        for i in range(1, heap.size):
            assert heap.heap_array[i] <= heap.heap_array[heap.get_parent_i(i)]

        array = [1, 12, 4, 3, 15, 17, 7, 12, 14, 14, 14, 15, 3, 13, 7]
        heap = Heap(priority_gt=lambda a, b: a < b)
        heap.heapify(array)

        assert heap.size == 15
        for i in range(1, heap.size):
            assert heap.heap_array[i] >= heap.heap_array[heap.get_parent_i(i)]

    def test_insert(self):
        """Test heap insertion."""
        heap = Heap()

        array = [20, 49, 43, 39, 26, 27, 46, 45, 10, 15, 11, 33, 14, 3, 37]
        heap.heapify(array)
        heap.insert(100500)

        assert heap.size == 16
        assert heap.heap_array[0] == 100500
        assert heap.top == 100500

        heap.insert(100501)

        assert heap.size == 17
        assert heap.heap_array[0] == 100501
        assert heap.top == 100501

        heap.insert(0)

        assert heap.size == 18
        assert heap.heap_array[0] == 100501
        assert heap.top == 100501

    def test_extract_top(self):
        """Test extract_top method."""
        heap = Heap()

        array = [33, 2, 46, 8, 49, 48, 13, 1, 13, 20]
        ordered = [1, 2, 8, 13, 13, 20, 33, 46, 48, 49]
        heap.heapify(array)

        size = len(array)

        while array:
            assert heap.size == size
            top = heap.extract_top()

            size -= 1
            assert heap.size == size
            assert top == ordered.pop()


class TestSolution:
    """Test Problem 2 solution."""

    @pytest.mark.parametrize('thread_a,thread_b,expected',
                             TEST_PRIORITY_TEST_CASES)
    def test_threads_priority(self, thread_a, thread_b, expected):
        """Test threads prioritization."""
        assert thread_priority_greater(thread_a, thread_b) == expected

    @pytest.mark.parametrize('input_,expected',
                             zip(EXAMPLE_INPUTS, EXAMPLE_OUTPUTS))
    def test_example_cases(self, input_, expected):
        """Test on example data from problem statement."""
        threads_count, jobs = input_

        assert schedule_jobs(threads_count, jobs) == expected

    @pytest.mark.parametrize('jobs_count', [10, 100, 1000, 10000])
    def test_zero_time_jobs(self, jobs_count):
        """
        Test case: all jobs take zero time to complete.

        With such conditions first thread takes all jobs.
        """
        jobs = [0 for _ in range(jobs_count)]
        expected = [(0, 0) for _ in range(jobs_count)]

        assert schedule_jobs(1, jobs) == expected
        assert schedule_jobs(2, jobs) == expected
        assert schedule_jobs(10, jobs) == expected

    @pytest.mark.parametrize('threads_count,jobs_count', [
        (2, 10), (4, 100), (8, 1000), (50, 10000)])
    def test_one_time_jobs(self, threads_count, jobs_count):
        """
        Test case: all jobs take time 1 to complete.

        With such conditions jobs are evenly paralleled between all threads.
        """
        jobs = [1 for _ in range(jobs_count)]
        expected = [
            (i % threads_count, i // threads_count) for i in range(jobs_count)]

        assert schedule_jobs(threads_count, jobs) == expected

    @pytest.mark.parametrize('jobs_count', [10, 100, 1000, 10000])
    def test_one_thread(self, jobs_count):
        """
        Test case: only one thread available.

        The starting time of i-th task would be sum of all previous jobs times.
        """
        jobs = [random.randrange(0, 100) for _ in range(jobs_count)]
        expected = [(0, sum(jobs[:i])) for i in range(jobs_count)]

        assert schedule_jobs(1, jobs) == expected
