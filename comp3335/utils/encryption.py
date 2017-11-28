import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import random
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
key1 = "th1keyshou1dbk3ptsdcr2t"


bs = AES.block_size


key = hashlib.sha256(key1.encode()).digest()

def _pad(s):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

def _unpad(s):
    return s[:-ord(s[len(s)-1:])]

def msg_encrypt(raw):
	try:
	    raw = _pad(raw) 
	    iv = Random.new().read(AES.block_size)
	    cipher = AES.new(key, AES.MODE_CBC, iv)
	    text = str(base64.b64encode(iv + cipher.encrypt(raw)), 'utf-8')
	    return text
	except ValueError:
		return ""


def msg_decrypt(enc):
	try:
	    enc = base64.b64decode(enc)
	    iv = enc[:AES.block_size]
	    cipher = AES.new(key, AES.MODE_CBC, iv)
	    return _unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
	except ValueError:
		return ""

def transform(key):
	return hashlib.sha256(key.encode()).digest()

def encrypt(raw, input_key):
	try:
	    raw = _pad(raw)
	    key = transform(input_key)
	    iv = Random.new().read(AES.block_size)
	    cipher = AES.new(key, AES.MODE_CBC, iv)
	    text = str(base64.b64encode(iv + cipher.encrypt(raw)), 'utf-8')
	    return text
	except ValueError:
		return ""

def decrypt(enc, input_key):
	try:
		enc = base64.b64decode(enc)
		key = transform(input_key)
		iv = enc[:AES.block_size]
		cipher = AES.new(key, AES.MODE_CBC, iv)
		return _unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')
	except ValueError:
		return ""


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
	#print(bs)
	salt = generate_salt()

	#print(msg_decrypt("EO1qoA/0f/BC3sGU55GiDhhT7UU1v1vZshMMoe0hD6c3zt2LanfE5fmMJq7BQOmS"))
	storage = [salt, hash_func(pwd, salt)]
	#print(storage)
	while True:
		a = input()
		encrypted = msg_encrypt(a)
		decrypted = msg_decrypt(encrypted)
		print(type(encrypted), len(decrypted))


		#print(a + " is encrypted as ")

		print(encrypted)
		#print(" is decrypted as " + decrypted)
		
		if hash_func(a, salt) == storage[1]:
			print("correct")
		else:
			print("incorrect")


if __name__ == "__main__":
	main()