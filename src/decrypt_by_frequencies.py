import operator
import string
from typing import Iterable
from collections import defaultdict
from frequencies import GERMAN_LETTER_FREQUENCIES, SORTED_BY_FREQUENCIES

LETTER_IN_ALPHABET = 26
SORTED_LETTERS = SORTED_BY_FREQUENCIES


def main(message: str) -> None:
    global SORTED_BY_FREQUENCIES
    textToDecrypt = normalizeMessage(message)
    letterCount = getLetterCount(textToDecrypt)
    decryptMessage = decryptMessageByFreq(
        textToDecrypt, letterCount, SORTED_BY_FREQUENCIES)
    return decryptMessage


def normalizeMessage(message):
    """ Handle the edge case of the lowercased ß with the uppercase one : ẞ (1E9E in unicode) """
    return message.replace('ß', 'ẞ').upper()


def getLetterCount(message, reverse=False):
    global SORTED_LETTERS
    letterCount = {letter: 0.0 for letter in SORTED_LETTERS}
    for letter in letterCount.keys():
        letterCount[letter] = message.count(letter)
    return sorted(letterCount.items(), key=operator.itemgetter(1), reverse=not(reverse))


def decryptMessageByFreq(message, letterCountValue, baseFrequency):
    for ((letter, _), letterInFreq) in zip(letterCountValue, baseFrequency):
        message = message.replace(
            letter, letterInFreq.lower())
    return normalizeMessage(message)

# ===============================================
# Try to break the encrytption without the key
# ===============================================


def positions_sorted_by_frequencies(positions: Iterable[int]):
    d = defaultdict(lambda: 0)

    # Count the position occurences
    for pos in positions:
        d[pos] += 1

    # Calculate the frequence for each position
    totalPositions = len(positions)
    for pos in d:
        d[pos] = round(d[pos] * 100 / totalPositions, 4)

    # Sort by frequency
    d = {k: v for (k, v) in sorted(
        d.items(), key=operator.itemgetter(1), reverse=True)}

    return d


def decrypt_by_frequencies(msg: Iterable[int], frequencies=SORTED_LETTERS) -> str:
    global LETTER_IN_ALPHABET

    msg_length = len(msg)
    positions_sorted_to_freq = positions_sorted_by_frequencies(msg)
    positions_sorted = list(positions_sorted_to_freq.keys())

    (position_per_letter, position_left) = divmod(
        len(positions_sorted), LETTER_IN_ALPHABET)
    # in case the message < len(ALPHABET)
    position_per_letter = max(position_per_letter, 1)

    decrypted_msg = [None] * msg_length
    for (i, letter) in enumerate(SORTED_LETTERS):
        for j in range(position_per_letter + (1 if position_left > 0 else 0)):
            index = i * position_per_letter + j
            # Guard to avoid list index out of range
            if(index >= len(positions_sorted)):
                break
            position = positions_sorted[index]
            matching_indexes = (
                pos for (pos, el) in enumerate(msg) if el == position)

            for matching_index in matching_indexes:
                decrypted_msg[matching_index] = letter

        position_left -= 1
    # TODO: fix why some element can be None
    decrypted_msg = [el if el != None else '-' for el in decrypted_msg]
    return ''.join(decrypted_msg)


if __name__ == "__main__":
    from implementierung import encrypt
    from image import Image

    key = Image('./src/assets/26_nuances_de_grey.png')
    msg = "abcdefghijklmnopqrstuvwxyz"

    encrypted = encrypt(key, msg)
    print(encrypted)
    decrypted = decrypt_by_frequencies(encrypted)
    print(''.join(decrypted))
