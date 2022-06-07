#Blynk App using Python
#Python Version 2.7.9
#Blynklib by vshymanskyy -version 0.2.0
#Blynk Script with Led created by RVN V.

import BlynkLib
import network
import utime as time
from machine import Pin


# ENter WIfi_SSID and WIFI_PASS
WIFI_SSID = 'WIFI_SSID'
WIFI_PASS = 'WIFI_PASS'
BLYNK_AUTH = 'Enter Your Auth Token'
# Initialize Blynk

print("Connecting to WiFi network '{}'".format(WIFI_SSID))
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    time.sleep(1)
    print('WiFi connect retry ...')

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
Led1 = Pin(2, Pin.OUT)
Led2 = Pin(5, Pin.OUT)
Led3 = Pin(21, Pin.OUT)
@blynk.ON('V2')
def On(value):
  Led1.value(not Led1.value())
@blynk.ON("V4")
def v4(param):
  Led2.value(not Led2.value())
@blynk.ON("V21")
def v21(param):
  Led3.value(not Led3.value())
@blynk.VIRTUAL_READ(2)
def my_read_handler():
    # this widget will show some time in seconds..
    blynk.virtual_write(2, int(time.time()))

while True:
    blynk.run()






