import math

def encryption(key, message):
    message = message.replace(' ', '-')

    keyCharList = [x for x in key]
    keyLenght = len(key)
    messageLenght = len(message)
    nullCharsCount = messageLenght % keyLenght

    if nullCharsCount != 0:
        message = message + ((keyLenght - nullCharsCount) * "-")

    rowsCount = int(math.ceil(messageLenght / keyLenght))
    rowKey = []
    # set row key
    for i in range(0, rowsCount):
        rowKey.append(keyCharList[i % keyLenght])

    s = 0
    m = 0
    n = 0
    MessageDict = {}
    totalRowDict = {}
    newList = []

    for k in rowKey:
        n += 1
        t = 0
        rowDict = {}
        for y in message[s: s + keyLenght]:
            rowDict[keyCharList[t]] = y
            t += 1

        totalRowDict[k] = rowDict.copy()

        if len(totalRowDict) == keyLenght or len(rowKey) == n:
            newList.append(totalRowDict)
            MessageDict[m] = totalRowDict.copy()
            totalRowDict.clear()
            m += 1

        s += keyLenght

    for u in MessageDict:
        for v in MessageDict[u]:
            MessageDict[u][v] = sorted(MessageDict[u][v].items(), key=lambda kv: (kv[0], kv[1]))

    cipherText = ""
    for i in range(0, keyLenght):
        for g in MessageDict:
            for h in MessageDict[g]:
                cipherText += MessageDict[g][h][i][1]

    return cipherText


def decryption(key, cipher):
    k = 0
    i = 0

    cipherLenght = len(cipher)
    cipherCharList = [x for x in cipher]

    keyLenght = len(key)

    rowsCount = int(math.ceil(cipherLenght / keyLenght))

    sortedKeyCharList = sorted([x for x in key])

    matrix = []
    for _ in range(rowsCount):
        matrix += [[None] * keyLenght]

        # fill matrice
    for _ in range(keyLenght):
        m = key.index(sortedKeyCharList[k])

        for j in range(rowsCount):
            matrix[j][m] = cipherCharList[i]
            i += 1
        k += 1
    plainText = ""
    for s in range(0, rowsCount):
        for t in range(0, keyLenght):
            plainText += matrix[s][t]

    return plainText
key = input("write key : ")
message = input("write message : ")

upperKey = key.upper()  # make upper
upperMessage = message.upper()  # make upper

cipher = encryption(upperKey, upperMessage)

print("Encrypt: " + cipher)

plainText = decryption(upperKey, cipher)

print("Decryption : " + plainText)