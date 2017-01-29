import pytest

from p3_tables import DisjointSetManager, perform_merges

EXAMPLE_INPUTS = (
    (
        [1, 1, 1, 1, 1],
        (
            (3, 5),
            (2, 4),
            (1, 4),
            (5, 4),
            (5, 3),
        ),
    ),
    (
        [10, 0, 5, 0, 3, 3],
        (
            (6, 6),
            (6, 5),
            (5, 4),
            (4, 3),
        ),
    ),
)
EXAMPLE_OUTPUTS = (
    [2, 2, 3, 5, 5],
    [10, 10, 10, 11],
)


class TestDisjointSetManager:
    """Test DisjointSetManager class realization."""

    def test_set_creation(self):
        """
        Test new set creation.

        Each new set must have unique id.
        """
        manager = DisjointSetManager()

        for i in range(10):
            manager.make_set(i)

        ids = set()

        for i in range(10):
            id_ = manager.find(i)
            ids.add(id_)

        assert len(ids) == 10, 'not all sets have unique id'

    def test_find(self):
        """Test find operation of set manager."""
        manager = DisjointSetManager()

        assert manager.find(0) is None
        assert manager.find(10) is None

        manager.make_set(0)
        assert manager.find(0) is not None
        assert manager.find(0) == manager.find(0)
        assert manager.find(10) is None

        manager.make_set(10)
        assert manager.find(10) is not None
        assert manager.find(10) == manager.find(10)
        assert manager.find(10) != manager.find(0)

    def test_union(self):
        """
        Test Union operation.

        Elements from both unioned sets must have same id.

        Union method must return new_root, new_subtree — ids of merged trees,
        where second new_subtree is now subtree of new_root.
        """
        manager = DisjointSetManager()

        for i in range(1, 13):
            manager.make_set(i)

        assert manager.union(2, 10) == (2, 10)
        assert manager.union(7, 5) == (7, 5)
        assert manager.union(6, 1) == (6, 1)
        assert manager.union(3, 4) == (3, 4)
        assert manager.union(5, 11) == (7, 11)
        assert manager.union(7, 8) == (7, 8)
        assert manager.union(7, 3) == (7, 3)
        assert manager.union(12, 2) == (2, 12)
        assert manager.union(9, 6) == (6, 9)

        # union of elements in the same set is noop
        assert manager.union(9, 6) == (None, None)
        assert manager.union(1, 1) == (None, None)

        # elements in same set MUST have same ids

        # first set: {2, 10, 12}
        id_first = manager.find(2)
        for i in (2, 10, 12):
            assert manager.find(i) == id_first, (
                "{i} not in first set".format(i))

        # second set: {1, 6, 9}
        id_second = manager.find(1)
        for i in (1, 6, 9):
            assert manager.find(i) == id_second, (
                "{i} not in first set".format(i))

        # third set: {3, 4, 5, 7, 8, 11}
        id_third = manager.find(3)
        for i in (3, 4, 5, 7, 8, 11):
            assert manager.find(i) == id_third, (
                "{i} not in third set".format(i))

        # this three sets must be different
        assert id_first != id_second
        assert id_first != id_third
        assert id_second != id_third


class TestSolution:
    """Test Problem 3 solution."""

    @pytest.mark.parametrize('input_data,expected',
                             zip(EXAMPLE_INPUTS, EXAMPLE_OUTPUTS))
    def test_solution(self, input_data, expected):
        """Test on example data from problem statement."""
        table_sizes, merges = input_data
        assert list(perform_merges(table_sizes, merges)) == expected
