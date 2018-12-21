
from vignere.View import View
from vignere.EncryptionModel import EncryptionModel
from vignere.CryptoManager import CryptoManager


class Controller:
    """The Controller that will orchestrate calls between the View and the Model"""

    def __init__(self):
        self.view = View()

    def start_app(self):
        print("Starting Cipher app...")

        command = self.view.main_menu()
        print("User requested command {}".format(command))

        self.handle_user_command(command)

    def handle_user_command(self, command):
        """Take action based on command input by user"""
        if command == "1":
            self.handle_encryption()
        elif command == "2":
            self.handle_decryption()
        else:
            raise Exception("Invalid input")

    def handle_encryption(self):
        """Execute the encrypt command requested by the user"""
        (plain_text, key) = self.view.get_encryption_data()

        model = EncryptionModel(plain_text, key)
        model.encrypted_text = CryptoManager.encrypt_string(model.plain_text, model.key)

        self.view.render_encyption_results(model)

    def handle_decryption(self):
        """Execute the decrypt command requested by the user"""
        self.view.get_decryption_data()


if __name__ == "__main__":
    c = Controller()
    c.start_app()