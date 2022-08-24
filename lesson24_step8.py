from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y_element = browser.find_element(By.ID, "answer")
    y = calc(x)
    y_element.send_keys(y)

    #people_checked = people_radio.get_attribute("checked")
    #print("value of people radio: ", people_checked)
    #assert people_checked is not None, "People radio is selected by default"
    #robots_checked = robots_radio.get_attribute("checked")
    #print("value of robots radio: ", robots_checked)
    #assert robots_checked is None, "Robots radio is not selected by default"

    button = browser.find_element(By.ID, "solve")
    button.click()    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.wait(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
    