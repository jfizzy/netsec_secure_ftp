from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class AESCipher:
    def __init__(self, key, iv):
        self._backend = default_backend()
        self._key = key
        self._iv = iv
        
    def init_suites(self):
        if self._key and self._iv:
            self._cs = Cipher(algorithms.AES(bytes(self._key, 'utf-8')), modes.CBC(self._iv), backend=self._backend) 
            self._encryptor = self._cs.encryptor()
            self._decryptor = self._cs.decryptor()
    
    def encrypt(self, plain_text):
        return self._encryptor.update(plain_text)

    def decrypt(self, cipher_text):
        return self._decryptor.update(cipher_text)

    def set_key(self, key):
        self._key = key

    def set_iv(self, iv):
        self._iv = iv
