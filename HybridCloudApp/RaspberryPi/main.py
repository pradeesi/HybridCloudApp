import paho.mqtt.client as mqtt
import ssl
import time
import json
import datetime
import Adafruit_DHT
import ConfigParser


SETTINGS_DIRECTORY = 'settings/'
SETTINGS_FILE_NAME = 'settings.ini'


def get_Settings(Section_Name):
	try:
		config = ConfigParser.ConfigParser()
		config.optionxform=str   #By default config returns keys from Settings file in lower case. This line preserves the case for keys
		config.read(SETTINGS_DIRECTORY + SETTINGS_FILE_NAME)
		
		return dict(config.items(Section_Name))	
	except Exception as error_msg:
		return {"Error" : str(error_msg)}
		

def read_DHT22_data(gpio_pin):

    # Read Humidity and Tempeature
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, gpio_pin)

    # Return humidity and temperature data
    return humidity, temperature


def prepare_sensor_data():
	try:
		# Read sensor data
		humidity, temperature = read_DHT22_data(SENSOR_GPIO_PIN) 
		
		# Prepare json paylod 
		sensor_data = {}
		sensor_data['SensorID'] = SENSOR_ID
		sensor_data['Location'] = CITY
		sensor_data['DateTime'] = str(datetime.datetime.utcnow())
		sensor_data['Temperature'] = temperature
		sensor_data['Humidity'] = humidity

		sensor_data_json = json.dumps(sensor_data)

		# Return Json Data
		return sensor_data_json
	except:
		print "Error in prepare_sensor_data"
		return None


settings = get_Settings('SENSOR_SETTINGS')

SENSOR_GPIO_PIN = int(settings['SENSOR_GPIO_PIN'])
CITY = settings['CITY']
SENSOR_ID = int(settings['SENSOR_ID'])
MQTT_PORT = int(settings['MQTT_PORT'])
SLEEP_INTERVAL = int(settings['SLEEP_INTERVAL'])
MQTT_KEEPALIVE_INTERVAL = int(settings['MQTT_KEEPALIVE_INTERVAL'])
MQTT_TOPIC = settings['MQTT_TOPIC']
MQTT_HOST = settings['MQTT_HOST']
CA_ROOT_CERT_FILE = SETTINGS_DIRECTORY + settings['CA_ROOT_CERT_FILE']
THING_CERT_FILE = SETTINGS_DIRECTORY + settings['THING_CERT_FILE']
THING_PRIVATE_KEY = SETTINGS_DIRECTORY + settings['THING_PRIVATE_KEY']



# This function will be triggered on successful MQTT connection
def on_connect(client, userdata, flags, rc):
	print ("Successfully Connected to AWS IoT Core...")


# Initiate MQTT Client
mqttc = mqtt.Client()

# Register publish callback function
mqttc.on_connect = on_connect

# Configure TLS Set
mqttc.tls_set(CA_ROOT_CERT_FILE, certfile=THING_CERT_FILE, keyfile=THING_PRIVATE_KEY, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

# Connect with MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)		
mqttc.loop_start()



while True:
	# Read Sensor Data
	sensor_data_json = prepare_sensor_data()
	# If Sensor data is not None
	if sensor_data_json:
		mqttc.publish(MQTT_TOPIC, sensor_data_json, qos=1)
	
	time.sleep(SLEEP_INTERVAL)


# Disconnect from MQTT_Broker
# mqttc.disconnect()


