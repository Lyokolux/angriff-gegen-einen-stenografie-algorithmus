from typing import Iterable
from random import choice
from image import Image


def encrypt(imageAsKey: Image, message: str) -> Iterable[int]:
    encryption_table = imageAsKey.getEncryptionTable()
    return [choice(encryption_table[ord(c)])
            for c in message]


def decrypt(imageAsKey: Image, encrypted: Iterable[int]) -> str:
    decryption_table = imageAsKey.getDecryptionTable()
    return ''.join((chr(decryption_table[x]) for x in encrypted))


def score(imageAsKey: Image, original: str, decrypted: str):
    return sum((1 for (char1, char2) in zip(original, decrypted) if char1 != char2))


if __name__ == "__main__":
    imagePath = 'src/assets/cover_image_coin.png'
    msg = 'helloworld'
    key = Image(imagePath)
    encrypted = encrypt(key, msg)
    decrypted = decrypt(key, encrypted)

    # Ensure that the encryption is working as expected
    assert score(key, msg, decrypted) == 0
