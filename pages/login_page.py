from .base_page import BasePage
from .base_page import get_random_string
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from .locators import MainPageLocators
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "This is not the login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self, email, password):
        fill_email = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        fill_email.send_keys(email)
        fill_pass1 = self.browser.find_element(*LoginPageLocators.PASS1_INPUT)
        fill_pass1.send_keys(password)
        fill_pass2 = self.browser.find_element(*LoginPageLocators.PASS2_INPUT)
        fill_pass2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
