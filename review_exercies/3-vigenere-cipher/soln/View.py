class View:

    def __init__(self):
        pass

    def main_menu(self):
        print("Please choose from the following")
        print("1. Encrypt")
        print("2. Decrypt")

        return input()

    def get_encryption_data(self):
        """Render the menu to get input from the user for the encypt operation"""
        print("Enter the plain text string")
        plain_text = input()

        print("Enter the key to be used")
        key = input()

        return (plain_text, key)

    def get_decryption_data(self):
        """"Render the menu to get user input for the decrypt operation"""
        encrypted_text = input("Enter the encrypted string")
        key = input("Enter the key")

        return (encrypted_text, key)

    def render_sub_menu(self):
        pass

    def render_encyption_results(self, encryption_model):
        print("The encrypted text is {} for plain text {} using key {}".format(encryption_model.encrypted_text, encryption_model.key, encryption_model.plain_text))
