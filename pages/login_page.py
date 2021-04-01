from .locators import LoginPageLocators
from .base_page import BasePage
import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        browser.find_element_by_id("login_link").click()
        WebDriverWait(browser, 5).until(
            ec.element_to_be_clickable((*MainPageLocators.LOGIN_USERMANE))
        LOGIN = browser.current_url(*MainPageLocators.LOGIN_LINK)
        assert LOGIN =="http://selenium1py.pythonanywhere.com/ru/accounts/login/" == True, "url адрес некорректен"

    def should_be_login_form(self):
        browser.find_element_by_id("login_link").click()
        WebDriverWait(br, 3).until(
            ec.element_to_be_clickable((*MainPageLocators.LOGIN_USERMANE)))
        WebDriverWait(br, 3).until(
            ec.element_to_be_clickable((*MainPageLocators.LOGIN_PASSWORD)))
        WebDriverWait(br, 3).until(
            ec.element_to_be_clickable((*MainPageLocators.LOGIN_SUBMIT)))
        # реализуйте проверку, что есть форма логина
        assert True, "Один из элементов формы не найден"

    def should_be_register_form(self):
        browser.find_element_by_id("login_link").click()
        WebDriverWait(br, 3).until(
            ec.element_to_be_clickable((*MainPageLocators.LOGIN_REG)))
        WebDriverWait(br, 3).until(
            ec.element_to_be_clickable((*MainPageLocators.LOGIN_REG_PAS1)))
        WebDriverWait(br, 3).until(
            ec.element_to_be_clickable((*MainPageLocators.LOGIN_REG_PAS2)))
        WebDriverWait(br, 3).until(
            ec.element_to_be_clickable((*MainPageLocators.LOGIN_REG_SUB)))
        # реализуйте проверку, что есть форма регистрации на странице
        assert True, "Один из элементов формы не найден"