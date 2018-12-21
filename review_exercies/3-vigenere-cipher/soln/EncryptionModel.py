
class EncryptionModel:
    """Holder/Model class for all things encryption. Is instantiated with the plain text string and the key and
    the encrypted text that will be computed later"""

    def __init__(self, plain_text, key):
        self.plain_text = plain_text
        self.key = key
        self.encrypted_text = None