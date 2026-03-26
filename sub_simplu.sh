#!/bin/bash

topic=$1
if [ -z $topic ]; then
	echo "folosire script:\n\tsub_simplu.sh [topic]"
	exit
fi

mosquitto_sub -h localhost -t $topic -v
