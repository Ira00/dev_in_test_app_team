from .page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        # Define locators specific to the LoginPage
        self.login_button_locator = (By.XPATH, "//*[@resource-id='com.ajaxsystems:id/authHelloLogin']")
        self.email_field_locator = (By.XPATH, "//*[@resource-id='com.ajaxsystems:id/authLoginEmail']//android.widget.EditText")
        self.password_field_locator = (By.XPATH, "//*[@resource-id='com.ajaxsystems:id/authLoginPassword']//android.widget.EditText")
        self.auth_login_button_locator = (By.XPATH, "//*[@resource-id='com.ajaxsystems:id/authLogin']")

    def click_login_button(self):
        self.click_element(self.login_button_locator)

    def click_auth_login_button(self):
        self.click_element(self.auth_login_button_locator)

    def send_email_data(self, data):
        element = self.find_element(self.email_field_locator)
        element.send_keys(data)

    def send_password_data(self, data):
        element = self.find_element(self.password_field_locator)
        element.send_keys(data)


