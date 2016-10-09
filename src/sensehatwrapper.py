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
        return WeatherData(int(self.sensehat.get_temperature()),
                           int(self.sensehat.get_humidity()),
                           int(self.sensehat.get_pressure()))

    def write_data_to_display(self):
        self.logger.debug('Writing weather data to display')
        self.sensehat.clear()
        self.sensehat.show_message(str(int(self.sensehat.get_temperature())) + ' C',
                                   text_colour=[28, 225, 239])