import blowfish
from os import urandom


cipher = blowfish.Cipher(b"pz key", byte_order = "little")
block = urandom(8)
print(block)
ciphertext = cipher.encrypt_block(block)
plaintext = cipher.decrypt_block(ciphertext)

print(ciphertext)
print(plaintext)
