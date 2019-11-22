#!/bin/bash
# Utility scripts.

SERVER=$(dirname ${BASH_SOURCE[0]})

# Quit on any error
set -e

# Run commands from context of server directory
cd $SERVER

# First time builds
if [ "$1" == "build" ]
then
	# Create and install packages into the virtual environment
	if [ ! -d ./env ] 
	then 
		python3 -m venv env
		source env/bin/activate
		pip install -r requirements.txt
	else
		source env/bin/activate
	fi

	# Run migrations on all the apps to build them into the database
	python server/manage.py makemigrations machines
	python server/manage.py migrate
fi

# If not running for build, we assume the virtual environment exists
source env/bin/activate

if [ "$1" == "createsuperuser" ]
then
	python server/manage.py createsuperuser
fi

# Run (but hang in terminal)
if [ "$1" == "run" ]
then
	if [ -z "$2" ]
	then
		PORT=4000
	else
		PORT=$2
	fi
	# Run the server on the specified port.
	python server/manage.py runserver $PORT
fi

# Run (with the nohup signal)
if [ "$1" == "start" ]
then
	if [ -z "$2" ]
	then
		PORT=4000
	else
		PORT=$2
	fi
	# Run the server on the specified port.
	nohup python server/manage.py runserver $PORT > server.log 2>&1 &
	echo $! > pid.txt
	# echo $PWD/env/bin/python server/manage.py runserver $PORT
fi

# Stop (using the pid)
if [ "$1" == "stop" ]
then
	# LINE=`ps ax | grep manage.py | awk '{print $1}'`
	kill `cat pid.txt`
fi