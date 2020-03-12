#!/bin/bash

if [ cat /dev/rfcomm0 = "runmain" ]; then
  echo "x has the value 'valid'"
fi