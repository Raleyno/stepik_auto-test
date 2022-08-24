from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    fname = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    fname.send_keys("Денис")
    lname = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    lname.send_keys("Фамилия")
    mail = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    mail.send_keys("test@tut.by")
    
    current_dir = os.path.abspath(os.path.dirname(__file__)) #("lesson22_step7.py"))
    # получаем путь к директории текущего исполняемого файла
    #print(current_dir)
    #print(os.path.abspath("load.txt")) 
    file_path = os.path.join(current_dir, 'load.txt')
    # добавляем к этому пути имя файла
    element = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    