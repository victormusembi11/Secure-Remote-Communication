from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import hashlib

def get_aes_cipher(key):
    key = hashlib.sha256(key.encode()).digest()
    return AES.new(key, AES.MODE_CBC)

def encrypt_message(message, key):
    cipher = get_aes_cipher(key)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode()
    ct = base64.b64encode(ct_bytes).decode()
    return iv + ":" + ct

def decrypt_message(encrypted, key):
    try:
        iv, ct = encrypted.split(":")
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = AES.new(hashlib.sha256(key.encode()).digest(), AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode()
    except:
        return None
