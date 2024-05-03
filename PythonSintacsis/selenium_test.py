import time
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
def open_page():
    browser.get('https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/index.php')
    bullet_car = browser.find_element(By.XPATH,"//*[contains(text(), 'Изменяет элемент.')]")
    print(bullet_car.text)

def test_open_page():
    open_page()

# для теста добавления файла в друг директорию пайтест
class A:
    x = 22
