import logging
import logging.config
import os.path

from flask import Flask
from flask import render_template
from apscheduler.schedulers.background import BackgroundScheduler
from datastore import DataStore
from sensehatwrapper import SenseHatWrapper

app = Flask(__name__)
app.config.update(
    ELASTICSEARCH_HOST='http://localhost:9200'
)
app.config.from_envvar('WEATHERSTATION_SETTINGS', silent=True)

logger = logging.getLogger()
datastore = DataStore(app.config['ELASTICSEARCH_HOST'])
sensehat = SenseHatWrapper()


def setup():
    # Set up logging
    logging.config.fileConfig(os.path.join(os.path.dirname(__file__), "logging.conf"))

setup()


def collect_data():
    logger.debug('Running data collection')
    weatherdata = sensehat.get_weather_data()
    datastore.save_data(weatherdata)


def update_display():
    logger.debug('Running display update')
    sensehat.write_data_to_display()

scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(collect_data, 'interval', minutes=1)
scheduler.add_job(update_display, 'interval', minutes=1)


@app.route('/')
def index():
    logger.debug('Calling app root')
    weatherdata = sensehat.get_weather_data()
    return render_template('index.html', weatherdata=weatherdata)
