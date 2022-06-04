#Controlling Led with ESP-32 using Webserver
#Micropython 2.7.6
#Created by RVN V.

from machine import Pin
import utime as time
import network
import socket


#AF_INT - user Internet protocol v4 addresses
#SOCK_STREAM - it is a TCP socket
#SOCK_DGRAM - it is a UDP socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8080))
s.listen(5)

# Entering Your WIFI ID and WIFI PASSWORD
WIFI_SSID = 'Your Wifi SSID'
WIFI_PASS = 'Your Wifi Password'

#Random Wierd Stuff HAHAHAHA
print("Connecting to Wifi newtork '{}'".format(WIFI_SSID))
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    time.sleep(1)
    print('Wifi connect retry ...')
print('Wifi IP:', wifi.ifconfig()[0])

#List of GPIO
relay_1 = Pin(2, Pin.OUT)
relay_1.off()
relay_2 = Pin(5, Pin.OUT)
relay_2.off()
relay_3 = Pin(21, Pin.OUT)
relay_3.off()

#List of Input Devices

def WebPage():
    
    if relay_1.value() == 1:
        LedState_1 = "ON"
        print("RELAY_1_on")
        
    else:
        LedState_1 = "OFF"
        print("RELAY_1_off")
    if relay_2.value() == 1:
        LedState_2 = "ON"
        print("RELAY_2_on")
        
    else:
        LedState_2 = "OFF"
        print("RELAY_2_off")
    if relay_3.value() == 1:
        LedState_3 = "ON"
        print("RELAY_3_on")
    else:
        LedState_3 = "OFF"
        print("RELAY_3_off") 
        
    page = """
    <html>
    <head>
        <meta content = "width = device-width, inital-scale = 1" name = "viewport"></meta>
    </head>
        <body>
            <center><h2>MY ESP32 Web Server</h2></center>
            <center>
                <form>
                    <a href="/?RELAY_1_on"><button name = "Relay 1" type = "submit" value = "1"> ON </a></button>
                    <a href="/?RELAY_1_off"><button name = "Relay 1" type = "submit" value = "0"> OFF </a></button>
                    </form>
                <form>
                    <a href="/?RELAY_2_on"><button name = "Relay 2" type = "submit" value = "1"> ON </a></button>
                    <a href="/?RELAY_2_off"><button name = "Relay 2" type = "submit" value = "0"> OFF </a></button>
                    </form>
                <form>
                    <a href="/?RELAY_3_on"><button name = "Relay 3" type = "submit" value = "1"> ON </a></button>
                    <a href="/?RELAY_3_off"><button name = "Relay 3" type = "submit" value = "0"> OFF </a></button>
                </form>
            </center>
            <center><p>Relay 1 is now <strong> """ + LedState_1 + """</strong></p></center>
            <center><p>Relay 2 is now <strong> """ + LedState_2 + """</strong></p></center>
            <center><p>Relay 3 is now <strong> """ + LedState_3 + """</strong></p></center>
        </body>
    </html>"""
    return page
    
  #main Program
while True:    
    # the socket accept
    conn, addr = s.accept()
    print("Got connection from %s" % str(addr))
    # the socket receive
    request = conn.recv(1024)
    print("")
    print("")
    print("Content %s" % str(request))
    # the socket send
    request = str(request)
    Relay1_On = request.find('/?RELAY_1_on')
    Relay1_Off = request.find('/?RELAY_1_off')
    Relay2_On = request.find('/?RELAY_2_on')
    Relay2_Off = request.find('/?RELAY_2_off')
    Relay3_On = request.find('/?RELAY_3_on')
    Relay3_Off = request.find('/?RELAY_3_off')
    
    if Relay1_On == 6:
        print("Led 1 is Active")
        LedState_1 = "ON"
        print(str(Relay1_On))
        relay_1.value(1)
        
    if Relay1_Off == 6:
        print("Led 1 is Inactive")
        print(str(Relay1_Off))
        relay_1.value(0)
        
    if Relay2_On == 6:
        print("Led 2 is Active")
        print(str(Relay2_On))
        relay_2.value(1)

    if Relay2_Off == 6:
        print("Led 2 is Inactive")
        print(str(Relay2_Off))
        relay_2.value(0)
        
    if Relay3_On == 6:
        print("Led 3 is Active")
        print(str(Relay3_On))
        relay_3.value(1)
        
    if Relay3_Off == 6:
        print("Led 3 is Inactive")
        print(str(Relay3_Off))
        relay_3.value(0)
    

    response = WebPage()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
    
    



