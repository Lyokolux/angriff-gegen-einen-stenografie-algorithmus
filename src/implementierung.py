from image import Image
from random import choice  # TODO: find one random enough for cryptographic usage

DIGIT_IN_BYTE = 8

# TODO: may ne faster with generator instead of list comprehension

# Use the bytearray as underlying low-level interface


def encrypt(imageAsKey: Image, message: str) -> bytearray:
    global DIGIT_IN_BYTE
    def convertToBinary(x): return format(x, 'b').zfill(DIGIT_IN_BYTE)

    encryption_table = imageAsKey.getEncryptionTable()
    message_as_ascii = [ord(c) for c in message]
    encrypted_as_position = [choice(encryption_table[c])
                             for c in message_as_ascii]
    return bytearray(encrypted_as_position)


def decrypt(imageAsKey: Image, encrypted: bytearray):
    global DIGIT_IN_BYTE
    character_in_message = len(encrypted) / DIGIT_IN_BYTE
    decryption_table = imageAsKey.getDecryptionTable()

    return ''.join([chr(decryption_table[x]) for x in encrypted])


if __name__ == "__main__":
    imagePath = 'src/assets/26_nuances_de_grey.png'
    key = Image(imagePath)
    print(decrypt(key, encrypt(key, 'helloworld')))
