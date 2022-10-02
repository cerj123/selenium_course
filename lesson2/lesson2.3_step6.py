import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    num1 = browser.find_element(By.ID, "input_value").text
    answer = calc(int(num1))

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(answer)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
