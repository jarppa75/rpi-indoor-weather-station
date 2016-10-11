#Raspberry Pi indoor weather station

Playing around with a Raspberry Pi and a Sense Hat

Will save data from the Sense Hat to ThingSpeak and update the LED Matrix and a web interface with the data.


###Setup

Install the Sense Hat by running the following commands on the Raspberry Pi:

    sudo apt-get update
    sudo apt-get install sense-hat
    sudo reboot
    
Install the dependencies for the app:

    sudo pip install -r requirements.txt
    
Create a file named production.py where you define these variables:

    THINGSPEAK_WRITE_KEY = '<ThingSpeak Write API Key>'
    THINGSPEAK_CHANNEL = '<ThingSpeak channel name>'

Create a channel in ThingSpeak that saves 3 values:

    https://se.mathworks.com/help/thingspeak/create-a-channel.html


###Run the application

    ./run-prod.sh 
