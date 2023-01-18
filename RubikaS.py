# RubikaS Beta

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://web.rubika.ir/#/login")

class RubikaS:
    def __init__(self):
        self.phonenumber = 0
        self.k = "abcdefghijklmnop"
        self.latest_message = ""

    def enter_phonenumber(self, phonenumber):
        time.sleep(1)
        phone = driver.find_element(By.NAME, "phone_number").send_keys(phonenumber)
        time.sleep(0.1)
        btn = driver.find_element(By.XPATH, "//app-root/tab-login/div/div/div/div/div/div/button/div/div")
        btn.click()
        return True

    def enter_password(self, password):
        time.sleep(1)
        driver.find_element(By.NAME, "phone_code").send_keys(password)
        return True

    def login(self, phonenumber):
        time.sleep(1)
        
        print()
        print()
        print()
        print()
        if self.enter_phonenumber(phonenumber):
            password = int(input("Enter the Password that is sent to your phone:"))
            if self.enter_password(password):
                return True
        return False

    def enter_chat(self):
        time.sleep(4)
        # print("CLICKING")
        el = driver.find_element(By.ID, "column-left")
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(el, 20, 5)
        action.click()
        action.perform()
        return True
    
    def check_message(self):
        time.sleep(1)
        while(True):
            lm = self.get_latest_message()
            # print(lm, "THIS", self.latest_message)
            if lm != self.latest_message and "ش" not in lm:
                self.latest_message = lm
                return True
            else:
                time.sleep(2)

    def get_latest_message(self):
        time.sleep(1)
        r = driver.find_elements(By.CLASS_NAME, "user-last-message")[2].text
        r = bytes.fromhex(r)
        return r

    def send(self, encrypted_message):
        time.sleep(1)
        message = driver.find_element(By.CLASS_NAME, "composer_rich_textarea").send_keys(encrypted_message[2:len(encrypted_message) - 1])
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, '.btn-icon.btn-send').click()
        return True

    def send_message(self, message):
        time.sleep(1)
        msg_text = message.encode("ASCII").rjust(0)
        print(msg_text)
        cipher = AES.new(self.k.encode('utf8'), AES.MODE_ECB)
        encoded = cipher.encrypt(pad(msg_text, 16)).hex()
        print("ENCODED", encoded)
        self.send(encoded)
        return True


    def recieve_message(self):
        encoded = self.get_latest_message()
        decipher = AES.new(self.k.encode('utf8'), AES.MODE_ECB)
        msg_dec = decipher.decrypt(encoded)
        rv = unpad(msg_dec, 16)
        return rv


def main():
    rubikaS = RubikaS()

    time.sleep(5)

    print("Welcome to RubikaS")
    time.sleep(1)
    print("Please Login to your account")
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    phonenumber = int(input("Your Phone number: "))
    rubikaS.phonenumber = phonenumber
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
