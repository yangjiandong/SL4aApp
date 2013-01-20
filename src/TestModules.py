# -*- coding: utf-8 -*-
# Default include for SL4A
import android
droid = android.Android()

action = "com.googlecode.android_scripting.action.LAUNCH_BACKGROUND_SCRIPT"
clsname = "com.googlecode.android_scripting"
pkgname = "com.googlecode.android_scripting.activity.ScriptingLayerServiceLauncher"
extras = {"com.googlecode.android_scripting.extra.SCRIPT_PATH":
         "/sdcard/sl4a/scripts/hello_world.py"}
myintent = droid.makeIntent(action, None, None, extras, None, clsname, pkgname).result
droid.startActivityIntent(myintent)