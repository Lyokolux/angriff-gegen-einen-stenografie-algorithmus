from image import Image
from random import choice  # TODO: find one random enough for cryptographic usage

DIGIT_IN_BYTE = 8


def encrypt(imageAsKey: Image, message: str) -> str:
    global DIGIT_IN_BYTE
    def convertToBinary(x): return format(x, 'b').zfill(DIGIT_IN_BYTE)

    encryption_table = imageAsKey.colorsMap
    message_as_ascii = [ord(c) for c in message]
    encrypted_as_position = [choice(encryption_table[c])
                             for c in message_as_ascii]
    encrypted_as_binary = [convertToBinary(x) for x in encrypted_as_position]
    return ''.join(encrypted_as_binary)


def decrypt(imageAsKey: Image, encrypted: str):
    global DIGIT_IN_BYTE
    character_in_message = len(encrypted) / DIGIT_IN_BYTE
    decryption_table = {position: code for code,
                        positions in imageAsKey.colorsMap.items() for position in positions}
    positions = [int(encrypted[step:step+DIGIT_IN_BYTE], 2)
                 for step in range(0, len(encrypted), DIGIT_IN_BYTE)]
    code = [decryption_table[x] for x in positions]
    return ''.join([chr(x) for x in code])


if __name__ == "__main__":
    imagePath = 'src/assets/26_nuances_de_grey.png'
    key = Image(imagePath)
    print(decrypt(key, encrypt(key, 'helloworld')))
