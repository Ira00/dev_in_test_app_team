from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def quit_browser(self):
        self.driver.quit()

