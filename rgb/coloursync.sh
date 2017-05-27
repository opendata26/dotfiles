#!/bin/sh

while true; do
	WALL="$(ls /home/opendata/Wallpapers |sort -R | tail -1)"
	case "$WALL" in
		"planet-blue.png") uchroma fx static --color=#03a9f4 && netcat 192.168.1.94 8888 <<< "3 169 244"
		;;
		"planet-green.png") uchroma fx static --color=#8bc34a && netcat 192.168.1.94 8888 <<< "50 195 20"
		;;
		"planet-indigo.png") uchroma fx static --color=#3f51b5 && netcat 192.168.1.94 8888 <<< "63 81 181" 
		;;
		"planet-orange.png") uchroma fx static --color=#ff5722 && netcat 192.168.1.94 8888 <<< "255 50 2"
		;;
		"planet-purple.png") uchroma fx static --color=#9c27b0 && netcat 192.168.1.94 8888 <<< "255 87 34" 
		;;
		"planet-red.png") uchroma fx static --color=#f44336 && netcat 192.168.1.94 8888 <<< "255 30 1"
		;;
	esac
	feh --bg-fill /home/opendata/Wallpapers/$WALL
	sleep 10m
done
