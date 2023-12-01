import pytest
from framework.main_page import MainPage


@pytest.fixture(scope='function')
def user_main_fixture(driver):
    login_page = MainPage(driver)
    yield login_page
    login_page.quit_browser()

