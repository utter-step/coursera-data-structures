import random

import pytest

from p3_patterns import poly_hasher, precompute_substring_hashes, rabin_karp

EXAMPLE_DATA = (
    ('aba', 'abacaba', [0, 4]),
    ('Test', 'testTesttesT', [4]),
    ('aaaaa', 'baaaaaaa', [1, 2, 3]),
)


class TestPolyHasher:
    """Test poly_hasher method."""

    @pytest.mark.parametrize('string', [
        'test', 'python', 'algo', 'hashes', 'test' * 1000])
    def test_equal_must_be_equal(self, string):
        """For equal strings hashes must be equal."""
        assert poly_hasher(
            string, 1337, 65537) == poly_hasher(string, 1337, 65537)


class TestPrecomputeSubstringHashes:
    """Test precompute_substring_hashes method."""

    @pytest.mark.parametrize('word,repetitions', [
        ('test', 200), ('hello w', 500), ('karppark', 1932)])
    def test_precompute_substring_hashes(self, word, repetitions):
        """Test precompute_substring_hashes method on repetative string."""
        p = 1000003
        x = 232332

        string = word * repetitions
        substr_hashes = precompute_substring_hashes(string, x, p, len(word))

        for i in range(len(substr_hashes) - len(word)):
            assert substr_hashes[i] == substr_hashes[i + len(word)]


class TestRabinKarp:
    """Test Rabin-Karp pattern matching algorithm realization."""

    @pytest.mark.parametrize('pattern,text,expected', EXAMPLE_DATA)
    def test_examples(self, pattern, text, expected):
        """Test cases given in problem statement."""
        assert list(rabin_karp(text, pattern)) == expected

    @pytest.mark.parametrize('text_length,pattern_length', [
        (1000, 10), (10000, 100), (10000, 1000), (100000, 1000)])
    def test_huge_similar(self, text_length, pattern_length):
        """Test large similar inputs."""
        text = 'a' * text_length
        pattern = 'a' * pattern_length

        assert list(rabin_karp(text, pattern)) == list(
            range(0, text_length - pattern_length + 1))

    @pytest.mark.parametrize('text_length,pattern_length', [
        (1000, 10), (10000, 10), (10000, 10), (100000, 12)])
    def test_random_input(self, text_length, pattern_length):
        """Test large random inputs."""
        random.seed(1337)
        text = ''.join(
            random.choice('ab')
            for _ in range(text_length)
        )
        pattern = ''.join(
            random.choice('ab')
            for _ in range(pattern_length)
        )

        occurencies = []
        for i in range(text_length - pattern_length):
            if text[i:i + pattern_length] == pattern:
                occurencies.append(i)

        assert len(occurencies) > 0
        assert list(rabin_karp(text, pattern)) == occurencies
