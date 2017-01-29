# python3


class DisjointSetManager(object):
    """Singleton class for managing disjoint set."""

    _parents = []
    _ranks = []

    def __init__(self, size=0):
        """Create new disjoint set manager with given size (default is 0)."""
        self._parents = [None] * size
        self._ranks = [None] * size

    def make_set(self, i):
        """Make new set containg only element i."""
        while i >= len(self._parents):
            self._parents.append(None)
        while i >= len(self._ranks):
            self._ranks.append(None)

        if self._parents[i] is not None:
            raise ValueError()

        self._parents[i] = i
        self._ranks[i] = 0

    def find(self, i):
        """Find id of set, containing element i."""
        if i >= len(self._parents) or self._parents[i] is None:
            return None

        visited = []
        while i != self._parents[i]:
            visited.append(i)
            i = self._parents[i]

        for v in visited:
            self._parents[v] = i

        return i

    def union(self, i, j):
        """
        Merge two sets containig elements i and j.

        Return ids of largest one and smallest one.
        """
        i_id = self.find(i)
        j_id = self.find(j)

        if i_id == j_id:
            return None, None

        rank_i = self._ranks[i_id]
        rank_j = self._ranks[j_id]
        new_root, new_subtree = None, None

        if rank_j > rank_i:
            new_root, new_subtree = j_id, i_id
        else:
            new_root, new_subtree = i_id, j_id
            if rank_i == rank_j:
                self._ranks[i_id] += 1

        self._parents[new_subtree] = new_root

        return new_root, new_subtree


def perform_merges(table_sizes, merges):
    """
    Perform merge operations on tables of the given sizes.

    After each merge yield size of currently largest table.
    """
    manager = DisjointSetManager()

    for i in range(len(table_sizes)):
        manager.make_set(i)

    max_size = max(table_sizes)

    for to, from_ in merges:
        to -= 1
        from_ -= 1

        merged_to, merged_from = manager.union(to, from_)

        if merged_to is not None:
            table_sizes[merged_to] += table_sizes[merged_from]
            table_sizes[merged_from] = 0

            max_size = max(max_size, table_sizes[merged_to])

        yield max_size

if __name__ == '__main__':
    n, m = map(int, input().split())

    table_sizes = list(map(int, input().split()))
    merges = [map(int, input().split()) for _ in range(m)]

    for max_size in perform_merges(table_sizes, merges):
        print(max_size)
