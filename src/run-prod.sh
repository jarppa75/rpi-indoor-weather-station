#!/bin/sh
unset WEATHERSTATION_SETTINGS
export WEATHERSTATION_SETTINGS=production.py
gunicorn weatherstation:app -p weatherstation.pid -b 0.0.0.0:8000 -D
