import logging
from weatherdata import WeatherData


class SenseHatWrapper:

    sensehat = None
    logger = logging.getLogger()

    def __init__(self):
        self.sensehat = None

    def get_weather_data(self):
        self.logger.debug('Fetching weather data')
        return WeatherData(42, 100, 99)

    def write_data_to_display(self):
        self.logger.debug('Writing weather data to display')