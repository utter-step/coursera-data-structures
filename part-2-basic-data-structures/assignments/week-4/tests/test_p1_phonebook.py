import pytest

from p1_phonebook import HashMap, perform_phonebook_operations


class TestHashMap:
    """Test HashMap realization."""

    def test_basics(self):
        """Test basic CRUD operations."""
        hmap = HashMap()

        hmap[1] = 'test'
        hmap[2] = 'test2'
        hmap[1] = 'test3'

        assert 1 in hmap
        assert 2 in hmap

        assert hmap[1] == 'test3'
        assert hmap[2] == 'test2'

        hmap.remove(1)
        assert 1 not in hmap
        assert 2 in hmap
        hmap.remove(1)
        assert 1 not in hmap
        assert 2 in hmap

        with pytest.raises(KeyError):
            hmap.get(1)

    def test_iterators(self):
        """Test keys, values and items iterators."""
        hmap = HashMap()

        for i in range(10):
            hmap[i] = i * i

        assert len(list(hmap.keys())) == 10
        assert len(list(hmap.values())) == 10
        assert len(list(hmap.items())) == 10

        for key in hmap.keys():
            assert key in hmap
            assert hmap[key] == key * key

        assert set(hmap.values()) == {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

        for key, value in hmap.items():
            assert key in hmap
            assert hmap[key] == value

        for i in range(5):
            hmap.remove(i * 2)

        assert len(list(hmap.keys())) == 5
        assert len(list(hmap.values())) == 5
        assert len(list(hmap.items())) == 5

        for key in hmap.keys():
            assert key in hmap
            assert hmap[key] == key * key

        assert set(hmap.values()) == {1, 9, 25, 49, 81}

        for key, value in hmap.items():
            assert key in hmap
            assert hmap[key] == value

    def test_load_factor(self):
        """
        Test load factor computation.

        Note the fact, that table resizes only up, not down.
        """
        hmap = HashMap()

        assert hmap.load_factor == 0

        for i in range(100):
            hmap[i] = i

        current_load = hmap.load_factor
        assert hmap.load_factor == hmap._size / hmap._len

        # after removing half of values, load should be halved too
        for i in range(50):
            hmap.remove(i * 2)
        assert hmap.load_factor == current_load / 2

        # removing keys that not in map should not affect load
        for i in range(50):
            hmap.remove(1337 + i * 13)
        assert hmap.load_factor == current_load / 2

        # if we clear the map, load should became 0
        for i in range(50):
            hmap.remove(i * 2 + 1)
        assert hmap.load_factor == 0

    @pytest.mark.parametrize('size', [1, 10, 100, 1000, 1024, 2048, 8192])
    def test_rehashing(self, size):
        """Verify that load factor does not exceed LOAD_FACTOR_LIMIT == 0.9."""
        assert HashMap.LOAD_FACTOR_LIMIT == 0.9
        hmap = HashMap()

        for i in range(size):
            hmap[i] = i ** 0.5
            assert hmap.load_factor < HashMap.LOAD_FACTOR_LIMIT


EXAMPLE_INPUTS = [
    (
        'add 911 police',
        'add 76213 Mom',
        'add 17239 Bob',
        'find 76213',
        'find 910',
        'find 911',
        'del 910',
        'del 911',
        'find 911',
        'find 76213',
        'add 76213 daddy',
        'find 76213',
    ),
    (
        'find 3839442',
        'add 123456 me',
        'add 0 granny',
        'find 0',
        'find 123456',
        'del 0',
        'del 0',
        'find 0',
    ),
]
EXAMPLE_OUTPUTS = [
    (
        'Mom',
        'not found',
        'police',
        'not found',
        'Mom',
        'daddy',
    ),
    (
        'not found',
        'granny',
        'me',
        'not found',
    ),
]


class TestSolution:
    """Test Problem 1 solution."""

    @pytest.mark.parametrize('operations,output',
                             zip(EXAMPLE_INPUTS, EXAMPLE_OUTPUTS))
    def test_example(self, operations, output):
        """Test cases given in problem statement."""
        assert tuple(perform_phonebook_operations(operations)) == output
