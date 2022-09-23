from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_in_basket(browser, language):
    browser.get(link+language+'/catalogue/coders-at-work_207/')
    time.sleep(10)
    assert browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
