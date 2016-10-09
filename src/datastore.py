import logging
from datetime import datetime
import time
from elasticsearch import Elasticsearch


class DataStore:

    logger = logging.getLogger()
    indexnamepattern = "weatherstation-"
    elasticsearchclient = None

    def __init__(self, elasticsearchhost):
        self.logger.info('Initiating elasticsearch host: ' + elasticsearchhost)
        self.elasticsearchclient = Elasticsearch(elasticsearchhost)

    def save_data(self, weatherdata):
        self.logger.debug('Save weather data to index')
        indexname = self.indexnamepattern + datetime.today().strftime('%Y.%m.%d')

        if not self.elasticsearchclient.indices.exists(index=indexname):
            self.elasticsearchclient.indices.create(index=indexname)

        self.elasticsearchclient.index(index=indexname,
                                        doc_type="weather",
                                        body={"temperature": weatherdata.temperature, "humidity": weatherdata.humidity, "barometricpressure": weatherdata.barometricpressure, "timestamp": int(time.time())})
