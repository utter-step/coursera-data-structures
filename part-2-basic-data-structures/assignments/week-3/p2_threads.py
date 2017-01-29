# python3


class Heap(object):
    """Heap class with arbitrary priority comparator."""

    def __init__(self, priority_gt=None):
        """Initialize heap with given priority comparator if needed."""
        if priority_gt is None:
            priority_gt = Heap._default_gt

        self._priority_gt = priority_gt
        self._heap = []

    def sift_up(self, i):
        """Sift element at index i up the tree."""
        parent_i = Heap.get_parent_i(i)

        while parent_i >= 0 and self.gt(self._heap[i], self._heap[parent_i]):
            self._heap[i], self._heap[parent_i] = (
                self._heap[parent_i], self._heap[i])
            i = parent_i
            parent_i = Heap.get_parent_i(i)

    def sift_down(self, i, size=None):
        """Sift element at index i down the tree."""
        if size is None:
            size = len(self.heap_array)
        was_swap = True

        gt = self.gt

        while was_swap:
            was_swap = False
            top_index = i

            left_child_i = Heap.get_left_child_i(i)
            if left_child_i < size and gt(
                    self._heap[left_child_i], self._heap[top_index]):
                top_index = left_child_i

            right_child_i = Heap.get_right_child_i(i)
            if right_child_i < size and gt(
                    self._heap[right_child_i], self._heap[top_index]):
                top_index = right_child_i

            if i != top_index and top_index < size:
                was_swap = True

                self._heap[i], self._heap[top_index] = (
                    self._heap[top_index], self._heap[i])
                i = top_index

    def insert(self, el):
        """Insert el to the correct position in heap."""
        self._heap.append(el)
        self.sift_up(len(self._heap) - 1)

    def extract_top(self):
        """Extract top element from heap and restructure heap afterwards."""
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        top_ = self._heap.pop()

        self.sift_down(0)
        return top_

    def remove(self, i):
        """Remove element at index i from heap."""
        self._heap[i] = self._heap[0]

        self.sift_up(i)
        self.extract_top()

    def replace(self, i, new_value):
        """Replace element at index i in heap and reorder heap."""
        old = self._heap[i]
        self._heap[i] = new_value
        if old < new_value:
            self.sift_up(i)
        elif old > new_value:
            self.sift_down(i)

    def heapify(self, array):
        """Reinitialize current heap using given array."""
        self._heap = array

        for i in range(len(self._heap) // 2, -1, -1):
            self.sift_down(i)

    @property
    def top(self):
        """Get top heap element."""
        return self._heap[0]

    @property
    def heap_array(self):
        """Get underlying heap array."""
        return self._heap

    @property
    def size(self):
        """Get size of heap (number of elements in it)."""
        return len(self._heap)

    @property
    def gt(self):
        """Priority comparator of current heap."""
        return self._priority_gt

    @staticmethod
    def _default_gt(a, b):
        """Default comparison operator for heap building."""
        return a > b

    @staticmethod
    def get_parent_i(i):
        """Get index for parent in 0-indexed heap."""
        return (i - 1) // 2

    @staticmethod
    def get_left_child_i(i):
        """Get index for left child in 0-indexed heap."""
        return i * 2 + 1

    @staticmethod
    def get_right_child_i(i):
        """Get index for right child in 0-indexed heap."""
        return i * 2 + 2


def thread_priority_greater(thread_a, thread_b):
    """
    Prioritize two threads.

    >>> thread_priority_greater((0, 0), (1, 0))
    True

    >>> thread_priority_greater((0, 1), (1, 0))
    False
    """
    (id_a, finish_time_a), (id_b, finish_time_b) = thread_a, thread_b

    if finish_time_a == finish_time_b:
        return id_a < id_b

    return finish_time_a < finish_time_b


def schedule_jobs(threads_count, jobs):
    """Problem 2 solution."""
    threads = [(i, 0) for i in range(threads_count)]
    threads_heap = Heap(priority_gt=thread_priority_greater)
    threads_heap.heapify(threads)

    jobs_schedule = []

    for job_time in jobs:
        (thread_id, finish_time) = threads_heap.extract_top()

        jobs_schedule.append((thread_id, finish_time))
        threads_heap.insert((thread_id, finish_time + job_time))

    return jobs_schedule


if __name__ == '__main__':
    threads_count, n_jobs = map(int, input().split())
    jobs = map(int, input().split())

    jobs_schedule = schedule_jobs(threads_count, jobs)

    for thread_id, starting_at in jobs_schedule:
        print(thread_id, starting_at)
