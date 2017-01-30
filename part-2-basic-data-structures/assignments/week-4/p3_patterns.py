# python3
import random

P = 2 ** 31 - 1


def poly_hasher(string, x, prime):
    """String poly hasher, going in straight, not reversed order."""
    hash_ = 0
    for c in string:
        hash_ = (hash_ * x + ord(c)) % prime

    return hash_


def precompute_substring_hashes(string, x, prime, substr_l):
    """Precompute hashes of each substring of length `substr_l` in `string`."""
    if substr_l > len(string):
        raise ValueError

    x_exp = pow(x, substr_l, prime)

    hashes = [poly_hasher(string[:substr_l], x, prime)]

    for i in range(0, len(string) - substr_l):
        add = ord(string[i + substr_l])
        remove = ord(string[i]) * x_exp
        hashes.append((x * hashes[i] + add - remove) % prime)

    return hashes


def rabin_karp(text, pattern):
    """Find all occurences of `pattern` in `text` using Rabin-Karp algo."""
    x = random.randrange(1, P)
    l = len(pattern)

    pattern_hash = poly_hasher(pattern, x, P)
    hashes = precompute_substring_hashes(text, x, P, l)

    for i, hash_ in enumerate(hashes):
        if hash_ == pattern_hash and text[i:i + l] == pattern:
            yield i


if __name__ == '__main__':
    pattern = input()
    text = input()

    occurences = rabin_karp(text, pattern)
    print(" ".join(map(str, occurences)))
