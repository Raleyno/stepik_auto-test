from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

#link = "http://suninjuly.github.io/registration1.html"
#    check_1nk(link)

class TestLnk(unittest.TestCase):
    def test_1nk1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        f_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input[required].form-control.first")
        l_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input[required].form-control.second")
        email = browser.find_element(By.CSS_SELECTOR, "div.first_block input[required].form-control.third")
        f_name.send_keys("Имя")
        l_name.send_keys("Фамилия")
        email.send_keys("test@tut.by")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        return welcome_text
    
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Congratulations! You have successfully registered!" == welcome_text
    #def test_abs1(self):
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Не заполнены все обязательные поля. Регистрация неуспешна")
    
        # закрываем браузер после всех манипуляций
        browser.quit()
    def test_1nk2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        f_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input[required].form-control.first")
        l_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input[required].form-control.second")
        email = browser.find_element(By.CSS_SELECTOR, "div.first_block input[required].form-control.third")
        f_name.send_keys("Имя")
        l_name.send_keys("Фамилия")
        email.send_keys("test@tut.by")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        return welcome_text
    
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Congratulations! You have successfully registered!" == welcome_text
    #def test_abs1(self):
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Не заполнены все обязательные поля. Регистрация неуспешна")
    
        # закрываем браузер после всех манипуляций
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()
	