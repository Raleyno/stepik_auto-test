from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    x = int(num1.text)
    y = int(num2.text)
    sum=str(x+y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum) # ищем элемент с суммой x+y
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
	