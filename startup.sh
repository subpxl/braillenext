#!/bin/bash
var=$(cat /dev/rfcomm0)
echo "$var"


if [[ $var = "add" ]]
then
    echo running main.py
    sudo python3 /home/pi/cashma/main.py
else
    echo not good
fi
