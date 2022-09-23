from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Choose from langs: (en/ru/es/...)')


@pytest.fixture()
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'until.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
