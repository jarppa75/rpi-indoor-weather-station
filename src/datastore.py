import logging
import thingspeak


class DataStore:

    logger = logging.getLogger()
    channel = None

    def __init__(self, channel_id, api_write_key):
        self.logger.info('Initiating thingspeak channel: ' + channel_id)
        self.channel = thingspeak.Channel(id=channel_id, write_key=api_write_key)

    def save_data(self, weatherdata):
        self.logger.debug('Save weather data to store')

        try:
            response = self.channel.update({1: weatherdata.temperature,
                                            2: weatherdata.humidity,
                                            3: weatherdata.barometricpressure})

            self.logger.debug('channel update response: ' + response)

        except Exception as ex:
            self.logger.error('Channel update failed: ' + ex.message)
