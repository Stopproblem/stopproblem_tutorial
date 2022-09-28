from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    REGISTRATION_FORM = (By.ID, 'register_form')
    AUTORIZATION_FORM = (By.ID, 'login_form')
    REGISTRATION_EMAIL = (By.NAME, 'registration-email')
    REGISTRATION_PASSWORD = (By.NAME, 'registration-password1')
    REGISTRATION_PASSWORD2 = (By.NAME, 'registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')
    AUTORIZATION_EMAIL = (By.NAME, 'login-username')
    AUTORIZATION_PASSWORD = (By.NAME, 'login-password')
    BUTTON_FORGET_PASSWORD = (By.XPATH, "//a[text()='Я забыл пароль']")
    AUTORIZATION_BUTTON = (By.NAME, 'login_submit')

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "[value='Добавить в корзину']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".breadcrumb li.active")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6 p.price_color")
    BASKET_PRICE_TOTAL = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner")
