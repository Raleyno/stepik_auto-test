from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
#import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) 

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # Переход на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y_element = browser.find_element(By.CSS_SELECTOR, "#answer")
    y = calc(x)
    y_element.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()    
    
finally:
    #копирование результата вычисления из всплывающего окна
    #alert = browser.switch_to.alert
    #rezult = alert.text.split(': ')[-1]
    #pyperclip.copy(rezult)  
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    