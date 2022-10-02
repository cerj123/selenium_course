from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    print(num1)
    x = int(num1)

    num2 = browser.find_element(By.ID, "num2").text
    print(num2)
    y = int(num2) 
    
    answer = str(x + y)
    print(answer)
    
    #select = Select(browser.find_element(By.TAG_NAME, "select"))
    #select.select_by_value(answer) 
    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, "[value='"+ answer + "']").click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()