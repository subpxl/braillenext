# Braillenext

[Braillenext](https://braillenext.web.app/) is an open-source project aimed at creating an assistive device for the visually impaired. This device uses a combination of Raspberry Pi, Arduino, and various sensors to detect text and objects, converting them into tactile feedback.

## Table of Contents

1. [Hardware Requirements](#hardware-requirements)
2. [Assembly Instructions](#assembly-instructions)
3. [Software Setup](#software-setup)
4. [Usage](#usage)
5. [Development](#development)

## Hardware Requirements

- Raspberry Pi Zero
- Arduino Nano
- LiDAR sensor
- Pi Camera
- Acrylic sheet (4 or 5mm)
- Strong adhesive
- Other electronic components as specified in the schematics
- Power supply (battery)

## Assembly Instructions

### Mechanical Assembly

1. Use CorelDRAW and a laser cutter to cut the acrylic sheets according to the provided drawings.
2. Assemble the cut parts as shown in the reference images.

### Electronic Assembly

1. Wire the Arduino Nano components according to the schematics.
2. Connect the Raspberry Pi Zero components as per the provided diagrams.
3. Set up a common power supply for both the Arduino and Raspberry Pi.

## Software Setup

### Arduino Setup

1. Connect the Arduino Nano to your PC.
2. Use the Arduino IDE to upload the LiDAR code to the Arduino Nano.
3. Test the Arduino setup (LiDAR and vibrating coin motor).

### Raspberry Pi Setup

1. Burn Raspberry Pi OS onto an SD card for the Raspberry Pi Zero.
2. Set up WiFi and SSH access.
3. SSH into the Raspberry Pi.
4. Update the device and install required packages:

   ```bash
   sudo apt-get update && sudo apt-get upgrade
   sudo apt-get install python3-pip
   # Install other required packages

5. Create a base folder for Braillenext.
6. Test the Raspberry Pi camera.
7. Run all installation commands as specified in the setup guide.
8. Test the Raspberry Pi Bluetooth connection with a phone.
9. Upload the Python code.

10. Test all components:

    - Camera functionality
    - Bluetooth connectivity
    - Google Cloud Vision API integration
    - Android app connectivity



## Android App Setup
    1. Install the Android app on a supported device.
    2. If the app is not available, build a new one from the .aia file using MIT App Inventor 2.


## Usage
    1. Open the Android app.
    2. Connect the app to the Raspberry Pi Zero via Bluetooth.
    3. Point the device at text or an object.
    4. Press the appropriate button (text or object) on the right side of the app.

## Development
    The current active branch is devs. Please use this branch for testing before merging.


## Cloning the Repository
    git clone git@github.com:subpxl/braillenext.git


## Bluetooth Connection
    To connect with Bluetooth:
```bash
sudo bluetoothctl
agent on
default-agent
scan on
pair [device_mac_address]
connect [device_mac_address]    
```


## Serial Communication
    - To send data via serial from the Raspberry Pi:
```bash
echo "Hello" > /dev/rfcomm0
```
    - To read from serial:

```bash
cat /dev/rfcomm0
```

    - To read and send a text file:

```bash
echo "$(<speech_test.txt)" > /dev/rfcomm0
```



## Additional Resources
    - LiDAR Arduino Library
    - MIT App Inventor 2
    - Braillenext App Project

## Contributing
    the project is open for any contributions and updates
    