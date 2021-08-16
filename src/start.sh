#!/bin/bash


if [ $FLASK_DEBUG = "true" ];
then
    echo "debug mode"
    export FLASK_ENV=development
    flask db migrate
    flask db upgrade
    flask run --host=0.0.0.0 --port=5000
else
    echo "prod mode"
    waitress-serve --port=5000 --call 'app:create_app'
fi