# -*- coding: utf-8 -*-
# Default include for SL4A
import android,time
droid = android.Android()

import ftplib
import time
import os

HOST = '192.168.1.81'
USER = 'user'
PASS = 'pass'
REMOTE = 'phone-sync'
LOCAL = '/sdcard/sl4a/scripts/ftp-sync'

#LOG = "/mnt/sdcard/sl4a/pydev.log"
#if os.path.exists(LOG) is False:
#    f = open(LOG, "w")
#    f.close()
#LOG = open(LOG, "a")

def log(self, message):
    """Log and print messages
    message -- Message to log
    """
    LOG.write(message)
    print message

from math import *

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    km = 6367 * c
    return km

# locating
# 运行后没反应
def testLocating():
    lat1 = 33.111111
    lon1 = 90.000000

    droid.startLocating()

    time.sleep(15)
    while True:
       loc = droid.readLocation().result
       if loc == {}:
           droid.makeToast('空。。。')
           loc = getLastKnownLocation().result
       if loc != {}:
           try:
               n = loc['gps']
           except KeyError:
               n = loc['network']
       la = n['latitude']
       lo = n['longitude']

       if haversine(la, lo, lat1, lon1) < 1:
           droid.toggleRingerSilentMode(True)
       else:
           droid.toggleRingerSilentMode(False)

def testSms():
    droid = android.Android()
    droid.startLocating()
    time.sleep(15)
    loc = droid.readLocation()
    droid.stopLocating()
    now = str(datetime.datetime.now())

    if 'gps' in loc.result:
        lat = str(loc.result['gps']['latitude'])
        lon = str(loc.result['gps']['longitude'])
    else:
        lat = str(loc.result['network']['latitude'])
        lon = str(loc.result['network']['longitude'])

    outString = 'I am here: ' + now + ' ' + lat + ' ' + lon

    droid.smsSend('13813590578', outstring)

def sms(msg='ok'):
    droid.smsSend('13813590578', msg)

def test():
    droid.makeToast('Hello,ddd0000,ZW,中文倪')
    #log("test...")
    print "Hello"

def ftp():
    if not os.path.exists(LOCAL):
        os.makedirs(LOCAL)

    while True:
        srv = ftplib.FTP(HOST)
        srv.login(USER, PASS)
        srv.cwd(REMOTE)

        os.chdir(LOCAL)

        remote = srv.nlst()
        local = os.listdir(os.curdir)
        for file in remote:
            if file not in local:
                srv.storlines('RETR ' + file,
                              open(file, 'w').write)

        srv.close()
        time.sleep(1)

if __name__ == '__main__':
    test()
    #testLocating()
    #testSms()
    #sms('我是可以发短信的...')
