from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.NAME, "firstname")
    firstname.send_keys("Ivan")
    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("Petrov")
    
    email = browser.find_element(By.NAME, "email")
    email.send_keys("test@test.com")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    file = browser.find_element(By.NAME, "file")
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла