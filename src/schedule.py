import time
import android

droid = android.Android()

SCHEDULE = '/sdcard/sl4a/scripts/schedule.txt'
#17:00 Time to head home!
#21:00 Put the trash out
#22:00 Set the alarm

# Parse the schedule into a dict.
alerts = dict()
for line in open(SCHEDULE, 'r').readlines():
    line = line.strip()
    if not line: continue
    t, msg = line.split(' ', 1)

    alerts[t] = msg

# Check the time periodically and handle alarms.
while True:
    t = time.strftime('%H:%M')
    if t in alerts:
        droid.vibrate()
        droid.makeToast(alerts[t])
        del alerts[t]

    time.sleep(5)