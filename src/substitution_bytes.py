from random import shuffle
from typing import List, Tuple, MutableMapping
from frequencies import SORTED_BY_FREQUENCIES


def generateKey() -> List[int]:
    key = list(range(256))
    shuffle(key)
    return key


def encryptMessage(message: bytearray, key: List[int]) -> List[int]:
    return [key[c] for c in message]


def encrypted_to_string(message: List[int]):
    return ''.join((chr(x) for x in encrypted_message))


if __name__ == "__main__":
    input_message = bytearray('abcdefghijklmnopqrstuvwxyzäöüß', 'utf-8')
    key = generateKey()
    encrypted_message = encryptMessage(input_message, key)
    print(encrypted_message)
    print(encrypted_to_string(encrypted_message))
