# BtEchoClient.py

#from btcom import *  # TigerJython
from btpycom import *  # Standard-Python (PC, Raspi, ...)
import time

def onStateChanged(state, msg):
    global reply
    if state == "CONNECTING":
        print ("Connecting", msg)
    elif state == "CONNECTION_FAILED":
        print ("Connection failed", msg)
    elif state == "CONNECTED":
        print ("Connected", msg)
    elif state == "DISCONNECTED":
        print ("Disconnected", msg)
    elif state == "MESSAGE":
        print ("Message", msg)
        reply = msg
       
serviceName = "EchoServer"
print ("Performing search for service name", serviceName)
client = BTClient(stateChanged = onStateChanged)
serverInfo = client.findService(serviceName, 20)
if serverInfo == None:
    print ("Service search failed")
else:
    print ("Got server info", serverInfo)
    if client.connect(serverInfo, 20):
        for n in range(0, 101):
            client.sendMessage(str(n))
            reply = ""
            while reply == "":
                time.sleep(0.001)
        client.disconnect()  




"""
    serverInfo = ("18:01:F1:06:E0:3A", 1)   // this is for my phone
    connect(serverInfo, 20)

This greatly decreases the connection delay.

 """

# http://www.python-exemplary.com/index_en.php?inhalt_links=navigation_en.inc.php&inhalt_mitte=raspi/en/bluetooth.inc.php