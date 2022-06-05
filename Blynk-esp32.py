#Raw code
#Blynk-lib-python by vshymanskyy
#Connecting Blynk Using MicroPython 2.7.9 or 3.4 greater


import BlynkLib
import network
import utime as time
from machine import Pin

#list of GPIO


# ENter WIfi_SSID and WIFI_PASS
WIFI_SSID = 'Enter Your WIFI SSID'
WIFI_PASS = 'Enter Your WIFI PASS'
BLYNK_AUTH = 'Enter Your Blynk Auth'
# Initialize Blynk

try:
#         blynk = BlynkLib.Blynk(BLYNK_AUTH, insecure=True)
        blynk = BlynkLib.Blynk(BLYNK_AUTH,
#        insecure=True,          # disable SSL/TLS
        server='blynk.cloud', # fra1.blynk.cloud or blynk.cloud
        port=80,                # set server port
        heartbeat=30,           # set heartbeat to 30 secs
        log=print              # use print function for debug logging
        )
except OSError as e:
    utime.sleep(3)
    restart_and_reconnect(e)
# Register Virtual Pins
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
    print('Current V1 value: {}'.format(value))

@blynk.VIRTUAL_READ(2)
def my_read_handler():
    # this widget will show some time in seconds..
    blynk.virtual_write(2, int(time.time()))

while True:
    blynk.run()

