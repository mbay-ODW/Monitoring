import base64

class CryptoHandler(object):
    def __init__(self):
        pass

    @staticmethod
    def encrypt(inputText):
        return base64.encodestring((inputText).encode()).decode().replace('\n', '')

    @staticmethod
    def decrypt(encryptedText):
        return base64.decodestring((encryptedText).encode()).decode().replace('\n', '')
