import pexpect

results = open("scan_results.txt", 'w')
child = pexpect.spawn("bluetoothctl")
child.send("scan on\n")
bdaddrs = []

try:
    while True:
        child.expect("Device (([0-9A-Fa-f]{2}:){5}([0-9A-Fa-f]{2}))")
        bdaddr = child.match.group(1)
        if bdaddr not in bdaddrs:
            bdaddrs.append(bdaddr)
            results.write(bdaddr+"\n")
except KeyboardInterrupt:
    child.close()
    results.close()