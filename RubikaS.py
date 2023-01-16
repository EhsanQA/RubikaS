# RubikaS Beta

import base64
from Crypto.Cipher import AES
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.maximize_window()

class RubikaS:
    def __init__(self, phonenumber):
        self.phonenumber = phonenumber
        self.k = b"1234567890123456"

    def enter_phonenumber(self, phonenumber):
        driver.get("https://web.rubika.ir/#/login")
        time.sleep(2)
        driver.find_element(By.NAME, "phone_number").send_keys("9034679802")
        time.sleep(2)
        btn = driver.find_element(By.XPATH, "//app-root/tab-login/div/div/div/div/div/div/button/div/div")
        btn.click()
        return True

    def enter_password(self, password):
        driver.find_element(By.NAME, "phone_code").send_keys(password)
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
                message = str(input("Enter the message: "))
                is_successful = rubikaS.send_message(message)
                if not is_successful:
                    print("ERROR CODE 3 >>> MESSAGE NOT SENT")
                


if __name__ == "__main__":
    main()
