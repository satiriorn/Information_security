def Vigenere_cipher_encrypt(plaintext, key):
    plain_ascii = [ord(letter) for letter in plaintext]
    key_ascii = [ord(letter) for letter in key]
    cipher_ascii = []
    for i in range(len(plain_ascii)):

        temp = plain_ascii[i]+key_ascii[i % len(key)]-97
        if temp>122:
            cipher_ascii.append(temp-26)
        else:
            cipher_ascii.append(temp)
    ciphertext = ''.join(chr(i) for i in cipher_ascii)
    return ciphertext

def Vigenere_cipher_decrypt(ciphertext, key):
    cipher_ascii = [ord(letter) for letter in ciphertext]
    key_ascii = [ord(letter) for letter in key]
    plain_ascii = []
    for i in range(len(cipher_ascii)):
        plain_ascii.append(((cipher_ascii[i]-key_ascii[i % len(key)]) % 26) +97)

    plaintext = ''.join(chr(i) for i in plain_ascii)
    return plaintext

def Single_permutauion_ciphers_encode(keyword, message, normalize=False):
    if normalize: message = ''.join(message.split())
    rows = len(message) // len(keyword)
    if len(message) % len(keyword) != 0:
        rows += 1
    indexes = sorted([(index, value) for index, value in enumerate(keyword)], key=lambda item: item[1])
    result = ''
    for row in range(rows):
        for index in indexes:
            position = index[0] * rows + row
            if position < len(message):
                result += message[position]
            else:
                result += ' '
    return result


def Single_permutauion_ciphers_decode(keyword, cipher):
    rows = len(cipher) // len(keyword)
    if len(cipher) % len(keyword) != 0:
        rows += 1

    indexes = sorted([(index, value) for index, value in enumerate(keyword)], key=lambda item: item[1])
    indexes = sorted([(index, value) for index, value in enumerate(indexes)], key=lambda item: item[1][0])
    result = ''

    for index in indexes:
        for row in range(rows):
            position = index[0] + len(keyword) * row
            if position < len(cipher):
                result += cipher[position]

    return result
s = Single_permutauion_ciphers_encode('Ісус', 'практична робота')
print(s)
print(Single_permutauion_ciphers_decode('Ісус', s))
v=Vigenere_cipher_encrypt('practuchna', 'Jesus help me')
print(v)
print(Vigenere_cipher_decrypt(v, 'Jesus help me'))