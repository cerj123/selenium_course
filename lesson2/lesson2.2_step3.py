import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()


def calc(arg):
    return str(math.log(abs(12 * math.sin(int(arg)))))


try:
    browser.get(link)
    num1 = browser.find_element(By.ID, "num1").text
    print(num1)
    x = int(num1)

    num2 = browser.find_element(By.ID, "num2").text
    print(num2)
    y = int(num2)

    answer = str(x + y)
    print(answer)

    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, "[value='" + answer + "']").click()

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
