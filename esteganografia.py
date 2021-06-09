import sys, hashlib
from PIL import Image

def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

hash_string = 'Mensagem escondida'

sha_signature = encrypt_string(hash_string)

for s in sha_signature:
    print("{:<2d}".format(int(s,16)), end=' ')
print()

