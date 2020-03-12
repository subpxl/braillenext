#!/bin/bash
$listen cat /dev/rfcomm0

if [ "$listen" = "runmain" ]; then
  echo "x has the value 'valid'"
fi