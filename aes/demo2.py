from Crypto.Cipher import AES
import base64


class Aescrypt():
    def __init__(self, key, model, iv):
        self.key = self.add_16(key)
        self.model = model
        self.iv = iv

    def add_16(self, par):
        if type(par) == str:
            par = par.encode()
        while len(par) % 16 != 0:
            par += b'\x00'
        return par

    def aesencrypt(self, text):
        text = self.add_16(text)
        if self.model == AES.MODE_CBC:
            self.aes = AES.new(self.key, self.model, self.iv)
        elif self.model == AES.MODE_ECB:
            self.aes = AES.new(self.key, self.model)
        self.encrypt_text = self.aes.encrypt(text)
        return self.encrypt_text

    def aesdecrypt(self, text):
        if self.model == AES.MODE_CBC:
            self.aes = AES.new(self.key, self.model, self.iv)
        elif self.model == AES.MODE_ECB:
            self.aes = AES.new(self.key, self.model)
        self.decrypt_text = self.aes.decrypt(text)
        self.decrypt_text = self.decrypt_text.strip(b"\x00")
        return self.decrypt_text


if __name__ == '__main__':
    passwd = "5fd28e8b2d6c8678"
    iv = '5fd28e8b2d6c8678'

    aescryptor = Aescrypt(passwd, AES.MODE_CBC, iv)  # CBC模式
    # aescryptor = Aescrypt(passwd,AES.MODE_ECB,"") # ECB模式
    text = "好好学习"
    en_text = aescryptor.aesencrypt(text)
    print("密文:", en_text)
    text = aescryptor.aesdecrypt(en_text)
    print("明文:", text)
