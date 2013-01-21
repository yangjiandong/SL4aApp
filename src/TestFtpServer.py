#ftp
# -*- coding: utf-8 -*-
import android
droid = android.Android()
import sys

sys.path.append('/sdcard/sl4a/libs/')

import socket, struct
import ftpserver

authorizer = ftpserver.DummyAuthorizer()
authorizer.add_anonymous('/sdcard/Download')
authorizer.add_user('user', 'password', '/sdcard/sl4a/scripts', perm='elradfmw')
handler = ftpserver.FTPHandler
handler.authorizer = authorizer
ipdec = droid.wifiGetConnectionInfo().result['ip_address']
ipstr = socket.inet_ntoa(struct.pack('L', ipdec))
droid.makeToast(ipstr)
server = ftpserver.FTPServer((ipstr, 8080), handler)
server.serve_forever()
