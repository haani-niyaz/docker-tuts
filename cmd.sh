#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ];
then
	echo 'Running Dev server'
 	exec python "/app/identidock.py"
elif [ "$ENV" = 'UNIT' ]; then
	echo 'Running Unit Tests'
	exec python "/app/test.py"
else
	echo 'Running Prod server'
	exec uwsgi --http 0.0.0.0:9090 --wsgi-file /app/identidock.py \
             --callable app --stats 0.0.0.0:9191
fi
