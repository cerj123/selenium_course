from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    num1 = browser.find_element(By.ID, "input_value").text
    #print(num1)

    answer = calc(int(num1))
    #print(answer)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(answer)

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()