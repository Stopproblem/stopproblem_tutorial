from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_in_basket(browser):
    browser.get(link)
    assert browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
