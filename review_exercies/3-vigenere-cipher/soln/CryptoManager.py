from vignere.EncryptionModel import EncryptionModel


class CryptoManager:

    @staticmethod
    def encrypt_string(plain_text, key):
        print("Method to encrypt {} using key {}".format(plain_text, key))

        encrypted_text = "MyEncryptedOutput"

        return encrypted_text