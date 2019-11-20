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
	python3 -m venv env
	source env/bin/activate
	pip install -r requirements.txt

	# Run migrations on all the apps to build them into the database
	cd server
	python manage.py makemigrations machines
	python manage.py migrate
	cd ..
fi

# If not running for build, we assume the virtual environment exists
source env/bin/activate

