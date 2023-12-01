import pytest
from framework.login_page import LoginPage


@pytest.fixture(scope='function')
def user_main_fixture(driver):
    login_page = LoginPage(driver)
    yield login_page
    login_page.quit_browser()

