import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser.get(link)
    num1 = browser.find_element(By.ID, "input_value").text

    answer = calc(int(num1))
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(answer)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
