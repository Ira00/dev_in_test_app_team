import subprocess
import time

import pytest
from appium import webdriver

from utils.android_utils import android_get_desired_capabilities
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )

    time.sleep(5)


@pytest.fixture(scope='function')
def driver(run_appium_server):
    options = UiAutomator2Options().load_capabilities(android_get_desired_capabilities())
    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
    yield driver


