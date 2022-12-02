#!/bin/bash

#curl -X POST -F 'session_key=2839' -F \
#  -F 'player_key=2939' \
#  -F 'time_list=1,4,5,6' \
#  -F 'loc_list=11 22,33 44,55 66,77 88' \
#  http://localhost:8000/locdata
#URL = "http://localhost:8000/locdata"

curl -c cookies.txt -b cookies.txt http://localhost:8000/locdata

token=`awk '/^[^#]/ { print $7; exit}' cookies.txt`

curl -c cookies.txt -b cookies.txt --data "sessionkey=2839&player_key=2939&time_list=1,4,5,6&loc_list=11 22,33 44,55 66,77 88&csrfmiddlewaretoken=$token" http://localhost:8000/locdata

