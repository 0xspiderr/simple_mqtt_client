#!/bin/bash

topic=$1
if [ -z $topic ]; then
	echo "scriptul are nevoie de un topic ca argument"
	exit
fi

mosquitto_sub -h localhost -t $topic -v
