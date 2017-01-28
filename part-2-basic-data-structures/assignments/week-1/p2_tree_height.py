# python3
from collections import deque


class Node(object):
    """Simple node class."""

    def __init__(self, value):
        """Create new node with given value."""
        self._value = value
        self._children = []
        self._parent = None

    def add_child(self, child):
        """Add child to node."""
        self._children.append(child)
        child._parent = self

    def set_parent(self, parent):
        """Set node parent."""
        parent.add_child(self)

    def depth_first_traversal(self):
        """Return all descendants in depth-first order."""
        stack = deque()
        stack.append(self)

        while stack:
            node = stack.pop()
            stack.extend(node.children)

            yield node

    def breadth_first_traversal(self):
        """Return all descendants in breadth-first order."""
        queue = deque()
        queue.append(self)

        while queue:
            node = queue.popleft()
            queue.extend(node.children)

            yield node

    def get_height(self):
        """Calculate node height."""
        queue = deque()
        queue.append((self, 1))

        max_height = 1

        while queue:
            node, height = queue.popleft()
            queue.extend(map(lambda child: (child, height + 1), node.children))

            max_height = max(max_height, height)

        return max_height

    def get_size(self):
        """Get size of node's subtree."""
        queue = deque()
        queue.append(self)

        size = 0
        while queue:
            node = queue.popleft()
            queue.extend(node.children)

            size += 1

        return size

    @property
    def children(self):
        """Get node childen."""
        return self._children

    @property
    def parent(self):
        """Get node parent."""
        return self._parent

    @property
    def value(self):
        """Get node value."""
        return self._value

    def __repr__(self):
        """Node representation method."""
        return 'Node({0})'.format(repr(self.value))


def get_tree_height(parents_list):
    """
    Given a tree represented as list of parents for each node get it's height.

    >>> get_tree_height([4, -1, 4, 1, 1])
    3

    >>> get_tree_height([-1, 0, 4, 0, 3])
    4
    """
    nodes = [Node(i) for i in range(len(parents_list))]

    root = None

    for node_i, parent in enumerate(parents_list):
        node = nodes[node_i]

        if parent == -1:
            root = node
        else:
            node.set_parent(nodes[parent])

    if root is not None:
        return root.get_height()
    else:
        return 0


def solve_string(tree_spec):
    """Solve Problem 2."""
    return get_tree_height(list(map(int, tree_spec.split())))


if __name__ == '__main__':
    n = input()
    tree_spec = input()

    print(solve_string(tree_spec))
