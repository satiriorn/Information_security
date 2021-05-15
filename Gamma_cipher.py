import string

alphabeth = list(string.ascii_lowercase)

def encrypt(text, gamma):
    textLen = len(text)
    gammaLen = len(gamma)

    keyText = []
    for i in range(textLen // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(textLen % gammaLen):
        keyText.append(gamma[i])
    code = []
    for i in range(textLen):
        code.append(alphabeth[(alphabeth.index(text[i]) + alphabeth.index(keyText[i])) % 26])

    return code

def decrypt(code, gamma):
    codeLen = len(code)
    gammaLen = len(gamma)

    keyText = []
    for i in range(codeLen // gammaLen):
        for symb in gamma:
            keyText.append(symb)
    for i in range(codeLen % gammaLen):
        keyText.append(gamma[i])
    text = []
    for i in range(codeLen):
        text.append(alphabeth[(alphabeth.index(code[i]) - alphabeth.index(keyText[i]) + 26) % 26])

    return text

a= encrypt("god", "go")
print(a)
print(decrypt(a, "go"))