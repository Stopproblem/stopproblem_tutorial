from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help='Choose from langs: (en/ru/es/...)')
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser')

@pytest.fixture()
def language(pytestconfig):
    return pytestconfig.getoption('language')

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('browser should be chrome or firefox')
    yield browser
    print('\n quit browser')
    browser.quit()
