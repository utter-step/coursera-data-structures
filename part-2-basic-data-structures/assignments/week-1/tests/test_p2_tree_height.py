import pytest

from p2_tree_height import Node, solve_string, get_tree_height


class TestNodeClass:
    """Node class tests."""

    def test_init(self):
        """Test node initialization."""
        node = Node('something')

        assert node.value == 'something'
        assert node.parent is None
        assert node.children == []

    def test_repr(self):
        """Test Node.__repr__ method."""
        node = Node('some value')

        assert repr(node) == 'Node(\'some value\')'

    def test_add_child(self):
        """Test Node.add_child method."""
        root = Node('Les')
        cathy = Node('Cathy')

        assert root.children == []
        assert cathy.parent is None

        root.add_child(cathy)

        assert cathy in root.children
        assert cathy.parent is root

    def test_set_parent(self):
        """Test Node.set_parent method."""
        root = Node('Les')
        cathy = Node('Cathy')

        assert root.children == []
        assert cathy.parent is None

        cathy.set_parent(root)

        assert cathy in root.children
        assert cathy.parent is root

    def test_depth_first_traversal(self):
        """Test Node.depth_first_traversal method."""
        root = Node('Les')

        cathy = Node('Cathy')
        alex = Node('Alex')
        frank = Node('Frank')
        cathy.add_child(alex)
        cathy.add_child(frank)
        cathy.set_parent(root)

        sam = Node('Sam')
        nancy = Node('Nancy')
        sam.add_child(nancy)
        sam.set_parent(root)

        violet = Node('Violet')
        tony = Node('Tony')
        wendy = Node('Wendy')
        violet.add_child(tony)
        violet.add_child(wendy)
        violet.set_parent(sam)

        assert list(root.depth_first_traversal()) == [
            root, sam, violet, wendy, tony, nancy, cathy, frank, alex
        ]

    def test_breadth_first_traversal(self):
        """Test Node.breadth_first_traversal method."""
        root = Node('Les')

        cathy = Node('Cathy')
        alex = Node('Alex')
        frank = Node('Frank')
        cathy.add_child(alex)
        cathy.add_child(frank)
        cathy.set_parent(root)

        sam = Node('Sam')
        nancy = Node('Nancy')
        sam.add_child(nancy)
        sam.set_parent(root)

        violet = Node('Violet')
        tony = Node('Tony')
        wendy = Node('Wendy')
        violet.add_child(tony)
        violet.add_child(wendy)
        violet.set_parent(sam)

        assert list(root.breadth_first_traversal()) == [
            root,
            cathy, sam,
            alex, frank,
            nancy, violet,
            tony, wendy
        ]

    def test_get_height(self):
        """Test Node.get_height method."""
        root = Node('Les')

        assert root.get_height() == 1

        cathy = Node('Cathy')
        cathy.add_child(Node('Alex'))
        cathy.add_child(Node('Frank'))
        cathy.set_parent(root)

        sam = Node('Sam')
        sam.add_child(Node('Nancy'))
        sam.set_parent(root)

        violet = Node('Violet')
        violet.add_child(Node('Tony'))
        violet.add_child(Node('Wendy'))
        violet.set_parent(sam)

        assert root.get_height() == 4
        assert cathy.get_height() == 2
        assert sam.get_height() == 3
        assert violet.get_height() == 2

    def test_get_size(self):
        """Test Node.get_size method."""
        root = Node('Les')

        assert root.get_size() == 1

        cathy = Node('Cathy')
        cathy.add_child(Node('Alex'))
        cathy.add_child(Node('Frank'))
        cathy.set_parent(root)

        sam = Node('Sam')
        sam.add_child(Node('Nancy'))
        sam.set_parent(root)

        violet = Node('Violet')
        violet.add_child(Node('Tony'))
        violet.add_child(Node('Wendy'))
        violet.set_parent(sam)

        assert root.get_size() == 9
        assert cathy.get_size() == 3
        assert sam.get_size() == 5
        assert violet.get_size() == 3


class TestSolution:
    """Test Problem 2 solution."""

    @pytest.mark.parametrize('example,expected', [
        ('4 -1 4 1 1', 3),
        ('-1 0 4 0 3', 4),
    ])
    def test_examples(self, example, expected):
        """Test examples given in problem statement."""
        assert solve_string(example) == expected

    def test_very_high(self):
        """Test case: very high tree."""
        height = 10 ** 5
        tree = [i - 1 for i in range(height)]

        assert get_tree_height(tree) == height

    def test_only_one_node(self):
        """Test case: tree consisting of a single node."""
        assert get_tree_height([-1]) == 1

    def test_large_flat_tree(self):
        """Test case: large tree with flat structure."""
        size = 10 ** 5
        tree = [0] * size
        tree[0] = -1

        assert get_tree_height(tree) == 2
