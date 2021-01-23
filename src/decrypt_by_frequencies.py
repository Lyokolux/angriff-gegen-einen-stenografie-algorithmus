import operator
import string
from collections import defaultdict
from frequencies import GERMAN_LETTER_FREQUENCIES, SORTED_BY_FREQUENCIES

LETTERS = SORTED_BY_FREQUENCIES


def main(message: str) -> None:
    global SORTED_BY_FREQUENCIES
    textToDecrypt = normalizeMessage(message)
    print(textToDecrypt)
    letterCount = getLetterCount(textToDecrypt)
    decryptMessage = decryptMessageByFreq(
        textToDecrypt, letterCount, SORTED_BY_FREQUENCIES)
    return decryptMessage


def normalizeMessage(message):
    """ Handle the edge case of the lowercased ß with the uppercase one : ẞ (1E9E in unicode) """
    return message.replace('ß', 'ẞ').upper()


def getLetterCount(message, reverse=False):
    global LETTERS
    letterCount = {letter: 0.0 for letter in LETTERS}
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


def positions_sorted_by_frequencies(positions: bytearray):
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


if __name__ == "__main__":
    from implementierung import encrypt
    from image import Image

    key = Image('./src/assets/26_nuances_de_grey.png')
    msg = "helloworld"

    encrypted = encrypt(key, msg)
