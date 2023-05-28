from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def go_to_basket(self):
        go_to_basket = self.browser.find_element(*BasePageLocators.BASKET_BTN)
        go_to_basket.click()

    def should_be_empty(self):
        assert self.is_not_element_present(*BasePageLocators.NOT_EMPTY_BASKET), "The basket is not empty"

    def should_be_empty_state(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET), "The empty state message is not present"
