#!/bin/bash
$cat /dev/rfcomm0 >> $listen

if [ "$listen" = "runmain" ]; then
  echo "x has the value 'valid'"
fi