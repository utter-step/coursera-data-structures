# python3
import random

P = 1000000007
X = 263

OPERATOR_ADD = 'add'
OPERATOR_DEL = 'del'
OPERATOR_FIND = 'find'
OPERATOR_CHECK = 'check'


def get_int_hasher(m, a=None, b=None):
    """Create arbitrary integer hasher with cardinality m."""
    if a is None:
        a = random.randrange(1, P)
    if b is None:
        b = random.randrange(0, P)

    def hasher(x):
        return ((a * x + b) % P) % m

    return hasher


def poly_hasher(s, x, p):
    """Get integer hash for string s from 0 to P-1."""
    hash_ = 0
    for c in reversed(s):
        hash_ = (hash_ * x + ord(c)) % p

    return hash_


def get_poly_hasher(x=None):
    """Create polynomial string hasher."""
    if x is None:
        x = random.randrange(1, P)

    def hasher(s):
        return poly_hasher(s, x, P)

    return hasher


def get_string_hasher(m, x=None):
    """Create string hasher with cardinality m."""
    h_p = get_poly_hasher(x)

    def hasher(s):
        return h_p(s) % m

    return hasher


class HashSet(object):
    """Realization of HashSet structure with chaining collision resolution."""

    LOAD_FACTOR_LIMIT = 0.9
    SIZE_MULTIPLIER = 2

    def __init__(self, resizable=True, initial_size=10,
                 hash_generator=None, generator_params=None):
        """Create new HashSet with option to specify hash func generator."""
        if hash_generator is None:
            hash_generator = HashSet._generic_hash_generator
        if generator_params is None:
            generator_params = {}

        self._resizable = resizable
        self._len = initial_size
        self._table = [None] * self._len
        self._size = 0
        self._generator_params = generator_params

        self._generator = hash_generator
        self._hasher = self._generator(self._len, **self._generator_params)

    def add(self, item, table=None):
        """Add new item-value pair to set or update existing."""
        if table is None:
            table = self._table

        hash_ = self._hasher(item)

        if table[hash_] is None:
            table[hash_] = [item]

        else:
            for i, item_ in enumerate(table[hash_]):
                if item_ == item:
                    return
            else:
                table[hash_].append(item)

        self._size += 1
        self._rehash()

    def remove(self, item):
        """Remove item-value pair from set, if exists."""
        hash_ = self._hasher(item)

        if self._table[hash_] is None:
            return

        for i, item_ in enumerate(self._table[hash_]):
            if item_ == item:
                break
        else:
            return

        self._table[hash_].pop(i)
        self._size -= 1

    def has_item(self, item):
        """Check if set contains given item."""
        hash_ = self._hasher(item)

        if self._table[hash_] is None:
            return False

        for i, item_ in enumerate(self._table[hash_]):
            if item_ == item:
                return True

        return False

    def _rehash(self):
        """
        Rehash table if it almost full.

        Resize underlying table if nescessary,
        create new hasher and reorder items accordingly.
        """
        if not self._resizable or self.load_factor < HashSet.LOAD_FACTOR_LIMIT:
            return

        self._len *= HashSet.SIZE_MULTIPLIER
        self._size = 0
        self._hasher = self._generator(self._len, **self._generator_params)
        new_table = [None] * self._len

        for item in self.items():
            self.add(item, new_table)

        self._table = new_table

    @staticmethod
    def _generic_hash_generator(m):
        hasher = get_int_hasher(m)

        def _hasher(obj):
            return hasher(hash(obj))

        return _hasher

    def items(self):
        """Return iterator over set's items."""
        for list_ in self._table:
            if list_ is None:
                continue

            for item in list_:
                yield item

    def get_table_line(self, i):
        """Return hash table line with given index."""
        return self._table[i]

    @property
    def load_factor(self):
        """Get table load factor, the ratio of stored pairs to table size."""
        return self._size / self._len

    # OPERATORS
    def __contains__(self, item):
        """Check if item is in set."""
        return self.has_item(item)  # noqa: W601

    def __iter__(self):
        """Iterator implementation."""
        for item in self.items():
            yield item


def perform_set_operations(set_size, operations):
    """
    Perform given operations on empty set.

    Return results of find and check operations.
    """
    hset = HashSet(resizable=False, generator_params={'x': X},
                   initial_size=set_size, hash_generator=get_string_hasher)

    for operation in map(lambda op: op.split(), operations):
        operator, operand = operation
        if operator == OPERATOR_ADD:
            hset.add(operand)

        elif operator == OPERATOR_CHECK:
            hash_line = hset.get_table_line(int(operand))

            if hash_line is None:
                yield ''
            else:
                yield ' '.join(reversed(hash_line))

        elif operator == OPERATOR_DEL:
            hset.remove(operand)

        elif operator == OPERATOR_FIND:
            yield 'yes' if operand in hset else 'no'

        else:
            raise ValueError('unknown operator: {0}'.format(operator))


if __name__ == '__main__':
    set_size = int(input())
    commands_count = int(input())

    operations = (input() for _ in range(commands_count))
    results = list(perform_set_operations(set_size, operations))

    for result in results:
        print(result)
