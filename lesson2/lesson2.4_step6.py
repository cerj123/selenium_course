from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

try:
	browser.get("http://suninjuly.github.io/cats.html")
	button = browser.find_element(By.ID, "button")

finally:
	browser.quit()
