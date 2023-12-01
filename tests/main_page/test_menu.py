from tests.login.test_login import login
import os
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_menu_bar_from_main_page(user_main_fixture, email=os.getenv('EMAIL'), password=os.getenv('PASSWORD')):
    login(user_main_fixture, email, password)
    logger.info(f'Looking for menu button')
    user_main_fixture.find_element(user_main_fixture.menu_button_locator, 30)
    user_main_fixture.click_menu_button()
    logger.info(f'Start testing. Settings in menu bar')
    user_main_fixture.find_settings_menu_button()
    logger.info(f'Start testing. Help in menu bar')
    user_main_fixture.find_help_menu_button()
    logger.info(f'Start testing. Logs in menu bar')
    user_main_fixture.find_logs_menu_button()
    logger.info(f'Start testing. Add Hub in menu bar')
    user_main_fixture.find_add_hub_menu_button()
    logger.info(f'End testing menu bar')