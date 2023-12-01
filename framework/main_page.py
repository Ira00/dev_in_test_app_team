from .login_page import LoginPage
from selenium.webdriver.common.by import By


class MainPage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.menu_button_locator = (By.XPATH, "//*[@resource-id='com.ajaxsystems:id/menuDrawer']")
        self.settings_menu_button_locator = (By.XPATH, "//*[@resource-id='com.ajaxsystems:id/settings']")
        self.help_menu_button_locator = (By.XPATH, "//*[@resource-id='com.ajaxsystems:id/help']")
        self.logs_menu_button_locator = (By.XPATH, "//*[@resource-id='com.ajaxsystems:id/logs']")
        self.add_hub_menu_button_locator = (By.XPATH, "//*[@resource-id='com.ajaxsystems:id/addHub']")

    def click_menu_button(self):
        self.click_element(self.menu_button_locator)

    def find_settings_menu_button(self):
        self.find_element(self.settings_menu_button_locator)

    def find_help_menu_button(self):
        self.find_element(self.help_menu_button_locator)

    def find_logs_menu_button(self):
        self.find_element(self.logs_menu_button_locator)

    def find_add_hub_menu_button(self):
        self.find_element(self.add_hub_menu_button_locator)


