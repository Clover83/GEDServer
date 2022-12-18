#!/bin/bash

SESSIONKEY="fdlspMQ2dPnLu2FrLS3i"
DEVICEID="testpkey2"
# TIMELIST is comma separated, do not include any whitespace or other characters.
TIMELIST="1,4,5"
# LOCLIST is comma separated, but contains x, y and z values
# which are space separated. Follow the formatting outlined here.
LOCLIST="0 0 0,3 3 3,4 4 4"

rm cookies.txt

curl -s -c cookies.txt -b cookies.txt http://localhost:8000/locdata/

token=`awk '/^[^#]/ { print $7; exit}' cookies.txt`

curl -c cookies.txt -b cookies.txt --data "session_key=$SESSIONKEY&player_key=$DEVICEID&time_list=$TIMELIST&loc_list=$LOCLIST&csrfmiddlewaretoken=$token" -X POST http://localhost:8000/locdata/

