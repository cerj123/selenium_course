import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()


def calc(arg):
    return str(math.log(abs(12 * math.sin(int(arg)))))


try:
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(answer)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()
    time.sleep(1)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
