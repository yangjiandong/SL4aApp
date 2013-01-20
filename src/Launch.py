#!/usr/bin/env python

import subprocess

ADB = r'D:\workspace\android\android-sdk-windows\platform-tools\adb.exe'
APPLICATION = 'TestFtpServer.py'#'downloads.py'#'TestHttpServer.py'
TARGET = '/mnt/sdcard/sl4a/scripts/'

def main():
    # Upload the application.
    subprocess.call([ADB, 'push', APPLICATION, TARGET + APPLICATION])

    # Launch the application.
    subprocess.call('"%s" shell am start \
                  -a com.googlecode.android_scripting.action.LAUNCH_BACKGROUND_SCRIPT \
                  -n \
                  com.googlecode.android_scripting/.activity.ScriptingLayerServiceLauncher \
                  -e com.googlecode.android_scripting.extra.SCRIPT_PATH \
                  "%s%s"' % (ADB, TARGET, APPLICATION))

if __name__ == '__main__':
    main()
