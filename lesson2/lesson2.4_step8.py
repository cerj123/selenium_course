import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    num1 = browser.find_element(By.ID, "input_value").text
    answer = calc(int(num1))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(answer)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()
