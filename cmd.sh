#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ];
then
	echo 'Running Dev server'
	exec uwsgi --http 0.0.0.0:9090 --catch-exceptions --wsgi-file /app/identidock.py \
             --callable app --stats 0.0.0.0:9191
else
	echo 'Running Prod server'
	exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/identidock.py \
             --callable app --stats 0.0.0.0:9191
fi
