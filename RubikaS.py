import base64
from Crypto.Cipher import AES
import time

class RubikaS:
    def __init__(self, phonenumber):
        self.phonenumber = phonenumber
        self.k = b"1234567890123456"

    def enter_phonenumber(self, phonenumber):
        # returns true if phone number is entered and waits for password
        return True

    def enter_password(self, password):
        # returns true if logged in successfully
        return True

    def login(self, phonenumber):
        password = int(input("Enter the Password that is sent to your phone:"))
        if self.enter_phonenumber(phonenumber):
            if self.enter_password(password):
                return True
        return False

    def enter_chat(self):
        # enters the first chat
        pass
    
    def check_message(self):
        # returns True if there's an unread message
        return True

    def get_latest_message(self):
        # returns the latest message that is sent to this user
        return b'gUhd9TxpnQppnZVAf7cv9mAR6wjufZUarqJvb+layjM='

    def send(self, encrypted_message):
        # sends the encrypted message and returns True if sending was successful
        return True

    def send_message(self, message):
        msg_text = message.encode("ASCII").rjust(32)
        cipher = AES.new(self.k ,AES.MODE_ECB) # never use ECB in strong systems obviously
        encoded = base64.b64encode(cipher.encrypt(msg_text))
        if self.send(encoded):
            return True
        return False


    def recieve_message(self):
        encoded = self.get_latest_message()
        cipher = AES.new(self.k ,AES.MODE_ECB)
        decoded = cipher.decrypt(base64.b64decode(encoded))
        return decoded


def main():

    print("Welcome to RubikaS")
    time.sleep(1)
    print("Please Login to your account")
    phonenumber = int(input("Your Phone number: "))
    rubikaS = RubikaS(phonenumber)
    if rubikaS.login(phonenumber):
        print("LOGGED IN TO YOUR ACCOUNT; YOU'RE NOW CHATTING:")
        print()
        print()
        rubikaS.enter_chat()
        while (True):
            time.sleep(0.5)
            if rubikaS.check_message():
                print(rubikaS.recieve_message())
    
            wants_to_send_message = str(input("Do you want to send a message? y/n "))
            if (wants_to_send_message == 'y'):
                message = str(input("Enter the message: "))
                is_successful = rubikaS.send_message(message)
                if not is_successful:
                    print("ERROR CODE 3 >>> MESSAGE NOT SENT")
                


if __name__ == "__main__":
    main()
