from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    people_radio = browser.find_element(By.ID, "peopleRule")
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_radio.click()
    check1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check1.click()
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    y_element = browser.find_element(By.CSS_SELECTOR, "#answer")
    y = calc(x)
    y_element.send_keys(y)

    #people_checked = people_radio.get_attribute("checked")
    #print("value of people radio: ", people_checked)
    #assert people_checked is not None, "People radio is selected by default"
    #robots_checked = robots_radio.get_attribute("checked")
    #print("value of robots radio: ", robots_checked)
    #assert robots_checked is None, "Robots radio is not selected by default"

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
	