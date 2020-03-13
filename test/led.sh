#!/bin/bash
#Exportamos el puerto GPIO 17 
echo 17 > /sys/class/gpio/export 
#Lo configuramos como salida 
echo out > /sys/class/gpio/gpio17/direction 
#Encendemos el LED asignandole 1 como valor lógico
echo 1 > /sys/class/gpio/gpio17/value