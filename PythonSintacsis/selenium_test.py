import time
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_open():
     browser.get('https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/index.php')
time.sleep(15)