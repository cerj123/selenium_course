import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    firstName = browser.find_element(By.CSS_SELECTOR, ".first:required")
    firstName.send_keys("Test")
    lastName = browser.find_element(By.CSS_SELECTOR, ".second:required")
    lastName.send_keys("Test")
    email = browser.find_element(By.CSS_SELECTOR, ".third:required")
    email.send_keys("test@test.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
