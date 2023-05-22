from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_correct_product(self):
        added_item_text = self.browser.find_element(*ProductPageLocators.ADDED_ITEM)
        item_name_text = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        print(added_item_text.text)
        print(item_name_text.text)
        assert added_item_text.text == item_name_text.text, "Added items are different"

    def should_be_correct_price(self):
        message_basket_total = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        print(product_price.text)
        print(message_basket_total.text)
        assert product_price.text == message_basket_total.text, "Prices are different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
