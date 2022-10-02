import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def answer(): 
    return math.log(int(time.time()))
links = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(3)
    browser.quit()


@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    link = f"https://stepik.org/lesson/{link}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    textarea = browser.find_element(By.TAG_NAME, "textarea")
    textarea.send_keys(answer())
    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    button.click()
    message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    assert "Correct!" in message.text
