#!/bin/sh
gunicorn weatherstation:app -p weatherstation.pid -b 0.0.0.0:8000 -D
