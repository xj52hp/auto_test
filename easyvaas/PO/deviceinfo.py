

class Getdeviceinfo():
    def get_deviceinfo(self):
        android_desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': 'm1 note',
            'appPackage': 'com.easyvaas.sqk',
            'noReset': 'true',
            'app': '/work/3qk.apk',
            'autoLaunch': 'true'
        }
        ios_desired_caps = {
            'platformName': 'iOS',
            'platformVersion': '10.3.0',
            'deviceName': 'iphone6s plus',
            'bundleID': 'com.easyvaas.kklive',
            'noReset': 'true',
            'app': '/work/3qk.ipa',
            'autoLaunch': 'true'
        }
        desired_caps = android_desired_caps
        return desired_caps
