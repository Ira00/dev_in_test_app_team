import os

import pytest
import logging
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def login(user_login_fixture, email, password):
    user_login_fixture.click_login_button()
    user_login_fixture.send_email_data(email)
    user_login_fixture.send_password_data(password)
    user_login_fixture.click_auth_login_button()


@pytest.mark.parametrize("email, password", [(os.getenv('EMAIL'), os.getenv('PASSWORD'))])
def test_positive_user_login(user_main_fixture, email, password):
    login(user_main_fixture, email, password)
    hub_element_locator = (By.XPATH, "//*[@resource-id='com.ajaxsystems:id/hubAdd']")
    assert user_main_fixture.find_element(hub_element_locator, 10).is_displayed()
    logger.info(f"Test positive_user_login with email: {email} and password: {password} passed.")


@pytest.mark.parametrize("email, password", [
    ("ajax@gmail.com", "password"),
    ("ajax.app@gmail.com", "qa_password")
])
def test_negative_user_login(user_main_fixture, email, password):
    login(user_main_fixture, email, password)
    snackbar_element_locator = (By.XPATH, "//*[@resource-id='com.ajaxsystems:id/snackbar_text']")
    assert user_main_fixture.find_element(snackbar_element_locator, 10).is_displayed()
    logger.info(f"Test negative_user_login with email: {email} and password: {password} passed.")


