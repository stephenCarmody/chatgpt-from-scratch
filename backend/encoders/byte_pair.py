# https://huggingface.co/learn/nlp-course/en/chapter6/5

import re


def bytes_to_unicode() -> dict:
    """Map bytes (0-255) to Unicode (character map)"""
    nice_charachters = (
        list(range(ord("!"), ord("~") + 1))
        + list(range(ord("¡"), ord("¬") + 1))
        + list(range(ord("®"), ord("ÿ") + 1))
    )
    unicode_points = nice_charachters[:]

    n = 0
    for byte in range(2**8):
        if byte not in nice_charachters:
            nice_charachters.append(byte)
            unicode_points.append(2**8 + n)
            n += 1

    print("unicode_points", unicode_points)

    unicode_points = [chr(i) for i in unicode_points]
    byte_to_char_map = dict(zip(nice_charachters, unicode_points))

    print("nice_charachters", nice_charachters)
    print("unicode_points", unicode_points)
    print("byte_to_char_map", byte_to_char_map)

    return byte_to_char_map


def get_pairs(word) -> set:
    """Uses a sliding window to get all pairs of characters in a word"""
    pairs = set()
    prev_char = word[0]
    for char in word[1:]:
        pairs.add((prev_char, char))
        prev_char = char
    return pairs


class Encoder:
    def __init__(self, encoder, bpe_merges):
        self.byte_encoder = bytes_to_unicode()
        self.byte_decoder = {v: k for k, v in self.byte_encoder.items()}

        self.encoder = encoder
        self.decoder = {v: k for k, v in self.encoder.items()}

        self.bpe_ranks = dict(zip(bpe_merges, range(len(bpe_merges))))

        self.pat = re.compile(
            r"""'s|'t|'re|'ve|'m|'ll|'d| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
        )
        self.cache = {}

    def bpe(self, token):

        if token in self.cache:
            return self.cache[token]

        # split the token into characters
        word = tuple(token)
        pairs = get_pairs(word)

        # if no pairs, return the token
        if not pairs:
            return token


if __name__ == "__main__":
    text = "This is some test text, let's see how it works"
    print(text)
    bytes_to_unicode()
