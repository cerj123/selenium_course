from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element(By.ID, "input_value").text
    #print(num1)

    answer = calc(int(num1))
    #print(answer)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(answer)
    
    option1 = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()