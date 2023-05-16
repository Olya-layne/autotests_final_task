import math
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def should_add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_success_message(self):
        self.browser.implicitly_wait(5)
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        assert success_message.text == (book_name.text + " has been added to your basket."), \
            "Couldn't find book name in success message"
        print(book_name.text + " - book name is correct!")

    def should_be_correct_amount(self):
        self.browser.implicitly_wait(5)
        basket_message = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE)
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        assert book_price.text in basket_message.text, "Couldn't find price in basket message"
        print(book_price.text + " - book price is correct!")
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")    
