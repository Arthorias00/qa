import time
# from selenium.webdriver.common.by import By
# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
import requests
# def test_equal():
#     assert 1 == 1, "number is not equal expected"
class TestClassDemoInstance:
    value = 0
    def test_one(self):
        self.value = 1
        assert self.value == 1
    def test_two(self):
        assert self.value == 1

# content of test_50.py
import pytest


@pytest.mark.parametrize("i", range(51))
def test_num(i):
    if i in (17, 25):
        pytest.fail("bad luck")
