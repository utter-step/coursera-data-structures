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


def sift_down(heap, i, gt, size=None):
    """Sift element at index i down the tree."""
    if size is None:
        size = len(heap)
    was_swap = True

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

            heap[i], heap[top_index] = heap[top_index], heap[i]
            i = top_index


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

    heapify(threads, gt=thread_priority_greater)

    jobs_log = []

    for job_time in jobs:
        (thread_id, finish_time) = extract_top(
            threads, gt=thread_priority_greater)

        jobs_log.append((thread_id, finish_time))
        insert(threads, (thread_id, finish_time + job_time),
               gt=thread_priority_greater)

    return jobs_log


if __name__ == '__main__':
    threads_count, n_jobs = map(int, input().split())
    jobs = map(int, input().split())

    jobs_log = schedule_jobs(threads_count, jobs)

    for thread_id, started_at in jobs_log:
        print(thread_id, started_at)
