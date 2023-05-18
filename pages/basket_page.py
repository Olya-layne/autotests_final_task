from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def basket_is_empty(self):
        assert self.element_is_not_present(*BasketPageLocators.BASKET_FORM)


    def basket_is_empty_message_is_present(self):
        basket_is_empty_message = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE)
        assert "Your basket is empty." in basket_is_empty_message.text, "No basket is empty message is present"
