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
