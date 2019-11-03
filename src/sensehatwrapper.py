import logging
from weatherdata import WeatherData
from sense_hat import SenseHat


class SenseHatWrapper:

    sensehat = None
    logger = logging.getLogger()

    def __init__(self):
        self.sensehat = SenseHat()

    def get_weather_data(self):
        self.logger.debug('Fetching weather data')
        return WeatherData(self.sensehat.get_temperature(),
                           self.sensehat.get_humidity(),
                           self.sensehat.get_pressure())

    def write_data_to_display(self):
        self.logger.debug('Writing weather data to display')
        self.sensehat.clear()
        self.sensehat.show_message(str(round(self.sensehat.get_temperature(), 1)) + ' C',
                                   text_colour=[28, 225, 239])