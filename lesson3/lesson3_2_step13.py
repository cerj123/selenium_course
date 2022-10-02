import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        try:
            browser.get(link)
            browser.implicitly_wait(5)

            first_name = browser.find_element(By.CSS_SELECTOR, ".first:required")
            first_name.send_keys("Test")
            last_name = browser.find_element(By.CSS_SELECTOR, ".second:required")
            last_name.send_keys("Test")
            email = browser.find_element(By.CSS_SELECTOR, ".third:required")
            email.send_keys("test@test.com")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        finally:
            browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        try:
            browser.get(link)
            browser.implicitly_wait(5)

            first_name = browser.find_element(By.CSS_SELECTOR, ".first:required")
            first_name.send_keys("Test")
            last_name = browser.find_element(By.CSS_SELECTOR, ".second:required")
            last_name.send_keys("Test")
            email = browser.find_element(By.CSS_SELECTOR, ".third:required")
            email.send_keys("test@test.com")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()
