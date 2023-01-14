import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def enter_phonenumber(phonenumber):
    driver.get("https://web.rubika.ir/#/login")

    time.sleep(2)


    driver.find_element(By.NAME, "phone_number").send_keys("9034679802")

    # driver.find_element(By.NAME, "KeyCode").send_keys("2741895139")

    time.sleep(2)

    btn = driver.find_element(By.XPATH, "//app-root/tab-login/div/div/div/div/div/div/button/div/div")
    btn.click()

def enter_password(password):
    driver.find_element(By.NAME, "phone_code").send_keys(password)

def open_first_chat():
    driver.find_element(By.XPATH, "//app-root/div/div/div/sidebar-container/div/sidebar-view/div/rb-chats/div/div/div/div/div/ul/li/div/div").click()


chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.maximize_window()

# enter_phonenumber()
# enter_password()
# open_first_chat()
