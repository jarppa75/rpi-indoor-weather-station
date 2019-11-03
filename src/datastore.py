import logging


class DataStore:

    logger = logging.getLogger()

    def __init__(self):
        self.logger.info('Initiating datastore. Currently not implemented')

    def save_data(self, weatherdata):
        self.logger.debug('Save weather data to store')

        try:
            self.logger.debug('Temperature ' + str(weatherdata.temperature) + ' Humidity ' + str(weatherdata.humidity) + ' barometric pressure ' + str(weatherdata.barometricpressure))
        except Exception as ex:
            self.logger.error('Data update failed: ' + ex.message)
