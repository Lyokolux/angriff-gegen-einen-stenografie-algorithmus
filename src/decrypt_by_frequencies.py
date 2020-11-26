import operator
import string
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


if __name__ == "__main__":
    mockedText = '\n'.join([letter * int(occurance*100) for (letter,
                                                             occurance) in GERMAN_LETTER_FREQUENCIES.items()])
    r = main(mockedText)
    # print(r)
