#!/bin/bash


if [ $# -lt 2 ]; then
	echo "folosire script:\n\tpub_simplu [mesaj] [topic]"
	exit
fi

mesaj=$1
topic=$2

mosquitto_pub -h localhost -m $mesaj -t $topic -d
