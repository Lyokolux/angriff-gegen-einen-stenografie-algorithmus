from random import shuffle
from typing import MutableMapping, Mapping
import string

NORMALIZE_TABLE: MutableMapping[str, str] = {
    'ß': 'ss',
    ''
}
# Add the punctuation (translated to an empty string)
NORMALIZE_TABLE.update({el: '' for el in string.punctuation})


def createAlphabet():
    return list(string.ascii_uppercase + 'ÄÜÖß')


def generateKey():
    alphabet = [letter for letter in createAlphabet()]
    shuffle(alphabet)
    return alphabet


def normalizeMessage(message: str, normalizeTable: Mapping[str, str] = NORMALIZE_TABLE) -> str:
    return ''.join([NORMALIZE_TABLE.get(char.upper(), char.upper()) for char in message])


def cryptText(text, encryptTable: Mapping[str, str]):
    return ''.join([encryptTable.get(char, char) for char in text])


if __name__ == "__main__":
    key = generateKey()
    encryptionTable = {k: v for (k, v) in zip(createAlphabet(), key)}
    textToEncrypt = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß abcdefghijklmopqrstuvwxyzäöüß $%&/.:,"
    textToEncrypt = normalizeMessage(textToEncrypt)
    cryptedText = cryptText(normalizeMessage(textToEncrypt), encryptionTable)
    print('\n'.join(cryptedText.split(' ')))
