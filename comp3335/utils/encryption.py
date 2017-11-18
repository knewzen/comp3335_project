import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import random
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class AESCipher(object):

    def __init__(self, key): 
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

c = AESCipher('shittyshittybangbang')

def hash_func(password, salt):
	new = password + salt
	new = new.encode('utf-8')
	string = hashlib.sha256(new).hexdigest()
	return string


def generate_salt():
	salt_len = 64
	salt = ''
	for i in range(salt_len):
		salt = salt + random.choice(ALPHABET)
	return salt





def main():
	pwd = "thereisnocipher"

	salt = generate_salt()

	storage = [salt, hash_func(pwd, salt)]
	print(storage)
	while True:
		a = input()
		encrypted = c.encrypt(a)
		decrypted = c.decrypt(encrypted)
		print(a + " is encrypted as ")
		print(encrypted)
		print(" is decrypted as " + decrypted)
		
		if hash_func(a, salt) == storage[1]:
			print("correct")
		else:
			print("incorrect")


if __name__ == "__main__":
	main()