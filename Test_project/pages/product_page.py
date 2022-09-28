from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_product_promo_url()
        self.should_be_add_to_basket_button()
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_product_promo_url(self):
        assert 'promo=newYear' in self.browser.current_url, 'promo not in url'

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'add to basket button not found'

    def should_be_product_price_is_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price_total = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_TOTAL).text
        assert product_price == basket_price_total, 'the price does not match'

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Message about adding is not found"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name in message, "No product name in the message"
