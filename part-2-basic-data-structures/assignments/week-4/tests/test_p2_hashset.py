import pytest

from p2_hashset import HashSet, get_string_hasher, perform_set_operations


EXAMPLE_INPUTS = (
    (
        5, (
            'add world',
            'add HellO',
            'check 4',
            'find World',
            'find world',
            'del world',
            'check 4',
            'del HellO',
            'add luck',
            'add GooD',
            'check 2',
            'del good',
        ),
    ),
    (
        4, (
            'add test',
            'add test',
            'find test',
            'del test',
            'find test',
            'find Test',
            'add Test',
            'find Test',
        ),
    ),
    (
        3, (
            'check 0',
            'find help',
            'add help',
            'add del',
            'add add',
            'find add',
            'find del',
            'del del',
            'find del',
            'check 0',
            'check 1',
            'check 2',
        ),
    ),
)

EXAMPLE_OUTPUTS = (
    (
        'HellO world',
        'no',
        'yes',
        'HellO',
        'GooD luck',
    ),
    (
        'yes',
        'no',
        'no',
        'yes',
    ),
    (
        '',
        'no',
        'yes',
        'yes',
        'no',
        '',
        'add help',
        '',
    ),
)


class TestHashSet:
    """Test HashSet realization."""

    def test_basics(self):
        """Test basic CRUD operations."""
        hset = HashSet()

        hset.add(1)
        hset.add(2)

        assert 1 in hset
        assert 2 in hset

        hset.remove(1)
        assert 1 not in hset
        assert 2 in hset
        hset.remove(1)
        assert 1 not in hset
        assert 2 in hset

    def test_iterators(self):
        """Test items iterator."""
        hset = HashSet()

        for i in range(10):
            hset.add(i)

        assert len(list(hset.items())) == 10
        for i in range(10):
            assert i in hset

        for el in hset:
            assert el in hset

        assert set(hset.items()) == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

    def test_load_factor(self):
        """
        Test load factor computation.

        Note the fact, that table resizes only up, not down.
        """
        hset = HashSet()

        assert hset.load_factor == 0

        for i in range(100):
            hset.add(i)

        current_load = hset.load_factor
        assert hset.load_factor == hset._size / hset._len

        # after removing half of values, load should be halved too
        for i in range(50):
            hset.remove(i * 2)
        assert hset.load_factor == current_load / 2

        # removing keys that not in set should not affect load
        for i in range(50):
            hset.remove(1337 + i * 13)
        assert hset.load_factor == current_load / 2

        # if we clear the set, load should became 0
        for i in range(50):
            hset.remove(i * 2 + 1)
        assert hset.load_factor == 0

    @pytest.mark.parametrize('size', [1, 10, 100, 1000, 1024, 2048, 8192])
    def test_rehashing(self, size):
        """Verify that load factor does not exceed LOAD_FACTOR_LIMIT == 0.9."""
        assert HashSet.LOAD_FACTOR_LIMIT == 0.9
        hset = HashSet()

        for i in range(size):
            hset.add(i)
            assert hset.load_factor < HashSet.LOAD_FACTOR_LIMIT

    def test_string_handling(self):
        """Test that string containing is working OK."""
        hset = HashSet(hash_generator=get_string_hasher)

        hset.add('aaa')
        hset.add('aab')
        hset.add('aba')
        hset.add('baa')

        assert len(list(hset.items())) == 4
        assert 'aaa' in hset
        assert 'aab' in hset
        assert 'aba' in hset
        assert 'baa' in hset

        assert set(hset.items()) == {'aaa', 'aab', 'aba', 'baa'}

        hset.remove('aaa')
        hset.remove('baa')
        hset.remove('bab')

        assert len(list(hset.items())) == 2
        assert 'aaa' not in hset
        assert 'aab' in hset
        assert 'aba' in hset
        assert 'baa' not in hset

        assert set(hset.items()) == {'aab', 'aba'}

    def test_initial_size(self):
        """Test that initial size sets correctly."""
        hset = HashSet(initial_size=20)

        assert len(hset._table) == 20
        hset.add(1)
        assert hset.load_factor == 0.05

    def test_not_resizable(self):
        """Test working with not resizable set."""
        hset = HashSet(resizable=False, initial_size=50)

        assert len(hset._table) == 50

        for i in range(1000):
            hset.add(i)
            assert len(hset._table) == 50
            assert hset.load_factor == (i + 1) / 50

    def test_get_table_line(self):
        """Test HashSet.get_table_line method."""
        hset = HashSet()

        for i in range(8):
            hset.add(i)

        for i in range(len(hset._table)):
            assert hset.get_table_line(i) == hset._table[i]

    @pytest.mark.parametrize('word,hash_value', [
        ('world', 4), ('HellO', 4), ('luck', 2), ('GooD', 2), ('good', 3)])
    def test_string_hasher(self, word, hash_value):
        """Test string polynomial hasher."""
        hasher = get_string_hasher(5, x=263)

        assert hasher(word) == hash_value


class TestSolution:
    """Test Problem 2 solution."""

    @pytest.mark.parametrize('input_,output',
                             zip(EXAMPLE_INPUTS, EXAMPLE_OUTPUTS))
    def test_example(self, input_, output):
        """Test cases given in problem statement."""
        set_size, operations = input_
        assert tuple(
            perform_set_operations(set_size, operations)) == output
