import subprocess


def android_get_desired_capabilities():
    adb_devices_output = subprocess.check_output(['adb', 'devices'], text=True)
    devices_info = [line.split('\t') for line in adb_devices_output.split('\n') if
                    line.strip() and not line.startswith('List of devices')]
    udid = devices_info[0][0] if devices_info else '11bd127d'
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': udid,
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }