import json
import re
import uuid
from collections import defaultdict
from faker import Faker
from implementierung import encryptWithTable, score_it
from frequencies import ENGLISH_SORTED_BY_FREQUENCIES
from decrypt_by_frequencies import decrypt_by_frequencies


def normalizeMessage(msg: str):
    return re.sub(r'[^a-z]', '', msg.lower())

# Structure of the json generated
# "size": {
#   "amountOfPosition": [
#        score1,
#        score2,
#        ...
#   ],
#   ...
# }
#


fake = Faker()

with open('src/assets/encryptionTable.json') as f:
    encryptionTables = json.loads(f.read())


def main(try_number):
    results = defaultdict(lambda: defaultdict(lambda: []))
    for maxTextLength in range(500, 1000):
        # print(textLength + textLength * 0.2 // 1, end='# ')
        msg = normalizeMessage(
            fake.text(max_nb_chars=maxTextLength))
        textLength = len(msg)
        for (position_per_letter, table) in enumerate(encryptionTables, 1):
            encrypted = encryptWithTable(table, msg)
            decrypted = decrypt_by_frequencies(
                encrypted, frequencies=ENGLISH_SORTED_BY_FREQUENCIES)

            score = score_it(msg, decrypted)
            results[textLength][position_per_letter].append(score)

        print(try_number, maxTextLength)
    return results


if __name__ == "__main__":
    for count in range(10):
        results = main(count)

        with open('src/angriff-results/' + str(uuid.uuid4()), 'w') as f:
            f.write(json.dumps(results))
        print('\n' + str(count))
