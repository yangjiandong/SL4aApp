# -*- coding: utf-8 -*-
import SimpleHTTPServer
from os import chdir
# Default include for SL4A
import android
droid = android.Android()
import socket,struct

ipdec = droid.wifiGetConnectionInfo().result['ip_address']
ipstr = socket.inet_ntoa(struct.pack('L', ipdec))


chdir('/sdcard/DCIM/Camera')
print "connect to %s" % ipstr
SimpleHTTPServer.test()
