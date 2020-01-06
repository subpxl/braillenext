
import sys
import bluetooth

uuid = "1e0ca4ea-299d-4335-93eb-27fcfe7fa848"

service_matches = bluetooth.find_service(address='18:01:F1:06:E0:3A')

if len(service_matches) == 0:
    print ("couldn't find the FooBar service")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to \"%s\" on %s" % (name, host))

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((host, port))
sock.send("hello!!")
sock.close()