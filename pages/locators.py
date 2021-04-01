from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # Вход
    LOGIN_USERMANE = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    LOGIN_SUBMIT = (By.TAG_NAME, '[name="login_submit"]')
    # Регистрация
    LOGIN_REG = (By.ID, "id_registration-email")
    LOGIN_REG_PAS1 = (By.ID, "id_registration-password1")
    LOGIN_REG_PAS2 = (By.ID, "registration-password2")
    LOGIN_REG_SUB = (By.ID, "registration_submit")
    