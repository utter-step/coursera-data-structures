# python3
import random

P = 2 ** 31 - 1

OPERATION_ADD = 'add'
OPERATION_DEL = 'del'
OPERATION_FIND = 'find'


def get_int_hasher(m):
    """Create arbitrary integer hasher."""
    a = random.randrange(1, P)
    b = random.randrange(0, P)

    def hasher(x):
        return ((a * x + b) % P) % m

    return hasher


class HashMap(object):
    """Realization of HashMap structure with chaining collision resolution."""

    LOAD_FACTOR_LIMIT = 0.9
    SIZE_MULTIPLIER = 2

    def __init__(self, hash_generator=None):
        """Create new HashMap with option to specify hash func generator."""
        if hash_generator is None:
            hash_generator = HashMap._generic_hash_generator

        self._len = 10
        self._table = [None] * self._len
        self._size = 0

        self._generator = hash_generator
        self._hasher = self._generator(self._len)

    def add_or_update(self, key, item, table=None):
        """Add new key-value pair to map or update existing."""
        if table is None:
            table = self._table

        hash_ = self._hasher(key)

        if table[hash_] is None:
            table[hash_] = [(key, item)]

        else:
            for i, (key_, item_) in enumerate(table[hash_]):
                if key_ == key:
                    table[hash_][i] = (key, item)
                    return
            else:
                table[hash_].append((key, item))

        self._size += 1
        self._rehash()

    def remove(self, key):
        """Remove key-value pair from map, if exists."""
        hash_ = self._hasher(key)

        if self._table[hash_] is None:
            return

        for i, (key_, item_) in enumerate(self._table[hash_]):
            if key_ == key:
                break
        else:
            return

        self._table[hash_].pop(i)
        self._size -= 1

    def get(self, key):
        """
        Get value from map by key.

        Raises KeyError, if key is not present.
        """
        hash_ = self._hasher(key)

        if self._table[hash_] is None:
            raise KeyError

        for i, (key_, item_) in enumerate(self._table[hash_]):
            if key_ == key:
                return item_

        raise KeyError

    def has_key(self, key):
        """Check if map contains given key."""
        hash_ = self._hasher(key)

        if self._table[hash_] is None:
            return False

        for i, (key_, item_) in enumerate(self._table[hash_]):
            if key_ == key:
                return True

        return False

    def _rehash(self):
        """
        Rehash table if it almost full.

        Resize underlying table if nescessary,
        create new hasher and reorder items accordingly.
        """
        if self.load_factor < HashMap.LOAD_FACTOR_LIMIT:
            return

        self._len *= HashMap.SIZE_MULTIPLIER
        self._size = 0
        self._hasher = self._generator(self._len)
        new_table = [None] * self._len

        for key, value in self.items():
            self.add_or_update(key, value, new_table)

        self._table = new_table

    @staticmethod
    def _generic_hash_generator(m):
        hasher = get_int_hasher(m)

        def _hasher(obj):
            return hasher(hash(obj))

        return _hasher

    def keys(self):
        """Return iterator over map's keys."""
        for list_ in self._table:
            if list_ is None:
                continue

            for key, value in list_:
                yield key

    def values(self):
        """Return iterator over map's values."""
        for list_ in self._table:
            if list_ is None:
                continue

            for key, value in list_:
                yield value

    def items(self):
        """
        Return iterator over map's key-value pairs.

        It would be better to implement this method as one for-loop, if somehow
        here is bottleneck (not likely).
        """
        return zip(self.keys(), self.values())

    @property
    def load_factor(self):
        """Get table load factor, the ratio of stored pairs to table size."""
        return self._size / self._len

    # OPERATORS
    def __contains__(self, key):
        """Check if key is in map."""
        return self.has_key(key)  # noqa: W601

    def __getitem__(self, key):
        """Get item via subscription syntax."""
        return self.get(key)

    def __setitem__(self, key, value):
        """Set item via subscription syntax."""
        return self.add_or_update(key, value)


def perform_phonebook_operations(operations):
    """
    Perform given sequence of operations on empty phonebook.

    Return generator with 'find' operations results.
    """
    phonebook = HashMap()

    for operation in map(lambda op: op.split(), operations):
        op_name = operation[0]
        phone = operation[1]

        if op_name == OPERATION_ADD:
            name = operation[2]
            phonebook[phone] = name
        elif op_name == OPERATION_DEL:
            phonebook.remove(phone)
        elif op_name == OPERATION_FIND:
            try:
                yield phonebook[phone]
            except KeyError:
                yield 'not found'
        else:
            raise ValueError('unknown op: {0}'.format(op_name))


if __name__ == '__main__':
    op_count = int(input())

    operations = (input() for _ in range(op_count))
    results = list(perform_phonebook_operations(operations))

    for result in results:
        print(result)
