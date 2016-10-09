#Raspberry Pi indoor weather station

Playing around with a Raspberry Pi and a Sense Hat

Will save data from the Sense Hat to Elasticsearch and update the LED Matrix and a web interface with the data.


###Setup

Install the Sense Hat by running the following commands on the Raspberry Pi:

    sudo apt-get update
    sudo apt-get install sense-hat
    sudo reboot
    
Install the dependencies for the app:

    sudo pip install -r requirements.txt
    
Create a file named production.py where you define this variable

    ELASTICSEARCH_HOST = '<url to your elasticsearch cluster>'


###Run the application

    ./run-prod.sh 
