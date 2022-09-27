from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

list_langs = ["es", "ru", "fr", "en"]


def pytest_add_option(parser):
    parser.addoption('--language', action='store', default='en', help='Choose from langs: (en/ru/es/...)')
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser')


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language in list_langs:
        print(f"\nstart chrome browser for {language} language test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be from the list " + str(list_langs))

    yield browser
    print("\nquit browser..")
    browser.quit()
