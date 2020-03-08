import bluetooth

bd_addr = "18:01:F1:06:E0:3A"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

try:
        sock.connect((bd_addr, port))
except :
    print("port1 failed")
else:
        sock.connect((bd_addr, 20))
finally:
    print("cant connect")

sock.send("hello!!")

sock.close()

"""
    serverInfo = ("18:01:F1:06:E0:3A", 1)   // this is for my phone
    connect(serverInfo, 20)

This greatly decreases the connection delay.

 """
