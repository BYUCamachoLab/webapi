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

# First time builds
if [ "$1" == "start" ]
then
	# Run migrations on all the apps to build them into the database
	python server/manage.py runserver
fi