from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    people_radio = browser.find_element(By.ID, "peopleRule")
    robots_radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_radio)
    robots_radio.click()
    check1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check1)
    check1.click()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
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
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    #with webdriver.Chrome() as browser:
    #link = "https://SunInJuly.github.io/execute_script.html"
    #browser.get(link)
    #button = browser.find_element(By.TAG_NAME, "button")
    #_ = button.location_once_scrolled_into_view
    #button.click()
	