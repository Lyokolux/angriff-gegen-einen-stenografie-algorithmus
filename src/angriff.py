import json
import re
import uuid
import sys
import os
import csv
import operator
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


def main(try_number):
    fake = Faker()
    with open('src/assets/encryptionTable.json') as f:
        encryptionTables = json.loads(f.read())
    results = defaultdict(lambda: defaultdict(lambda: []))

    for maxTextLength in range(500, 1000):
        msg = normalizeMessage(
            fake.text(max_nb_chars=maxTextLength))
        textLength = len(msg)

        for (position_per_letter, table) in enumerate(encryptionTables, 1):
            encrypted = encryptWithTable(table, msg)
            decrypted = decrypt_by_frequencies(
                encrypted, frequencies=ENGLISH_SORTED_BY_FREQUENCIES)

            score = score_it(msg, decrypted)
            results[textLength][position_per_letter].append(score)

    return results


def reduce_results(path):
    SUMMARY_FILE = 'summary'
    summary = defaultdict(lambda: defaultdict(lambda: []))

    # Read and populate
    for (i, result_file) in enumerate(os.listdir(path), 1):
        # Read file
        with open(os.path.join(path, result_file)) as f:
            content = json.loads(f.read())

        # Populate summary
        for (msgSize, positions) in content.items():
            for (amountOfPosition, scores) in positions.items():
                summary[msgSize][amountOfPosition].extend(scores)

    # Reduce summary
    summary = dict(summary)
    for (msgSize, positions) in summary.items():
        summary[msgSize] = dict(summary[msgSize])
        for (amountOfPosition, scores) in positions.items():
            summary[msgSize][amountOfPosition] = int(sum(scores) / len(scores))

    with open('src/results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Text Length', *list(summary.values())[0].keys()])
        for (msgSize, positionsWithScore) in sorted(summary.items(), key=lambda item: int(item[0])):
            writer.writerow([msgSize, *summary[msgSize].values()])


if __name__ == "__main__":
    DIR_PATH = 'src/angriff-results'
    argument = sys.argv[-1]

    if argument == 'generate':
        for count in range(10):
            results = main(count)

            with open(DIR_PATH + str(uuid.uuid4()), 'w') as f:
                f.write(json.dumps(results))
    elif argument == 'reduce':
        reduce_results(DIR_PATH)
    else:
        print("Argument unkown or inexistant")
