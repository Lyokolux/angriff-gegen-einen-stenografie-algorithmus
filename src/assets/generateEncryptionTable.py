import json

encryptionTables = []

for amounfOfPositionPerByte in range(1, 25):
    encryptionTable = []
    lastUsedPositionForByte = 0
    for byteValue in range(256):
        encryptionTable.append([])
        # Add one by default to shift the position
        for position in range(amounfOfPositionPerByte):
            encryptionTable[byteValue].append(lastUsedPositionForByte)
            lastUsedPositionForByte += 1

    encryptionTables.append(encryptionTable)

with open('encryptionTable.json', 'w') as f:
    f.write(json.dumps(encryptionTables, indent=2))
