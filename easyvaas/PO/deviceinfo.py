

class Getdeviceinfo():
    def get_deviceinfo(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': 'm1 note',
            'appPackage': 'com.easyvaas.sqk',
            'noReset': 'true',
            'app': '/work/3qk.apk',
            'autoLaunch': 'true'
        }
        return desired_caps
