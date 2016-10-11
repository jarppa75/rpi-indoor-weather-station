unset WEATHERSTATION_SETTINGS
export WEATHERSTATION_SETTINGS=development.py
export FLASK_APP=weatherstation.py
flask run --host 0.0.0.0 --port 8000
