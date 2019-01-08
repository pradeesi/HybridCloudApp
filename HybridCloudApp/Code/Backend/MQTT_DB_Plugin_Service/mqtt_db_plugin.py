import paho.mqtt.client as mqtt
import ssl
import time
import json
import datetime
import ConfigParser
import atexit
from mariadb_con_mqtt_db_plugin import Sensor_DB_Class
import os

#=============================================================
#===== READ SETTINGS ======
#=============================================================
SETTINGS_FILE_NAME = 'settings.ini'

DB_PASSWORD = str(os.environ['DB_PASSWORD'])

def get_Settings(Section_Name):
	try:
		config = ConfigParser.ConfigParser()
		config.optionxform=str   #By default config returns keys from Settings file in lower case. This line preserves the case for keys
		config.read(SETTINGS_FILE_NAME)
		
		return dict(config.items(Section_Name))	
	except Exception as error_msg:
		return {"Error" : str(error_msg)}

# Read AWS IoT Settings settings from settings.ini file
aws_settings = get_Settings('AWS_IOT_SETTINGS')

MQTT_PORT = int(aws_settings['MQTT_PORT'])
MQTT_KEEPALIVE_INTERVAL = int(aws_settings['MQTT_KEEPALIVE_INTERVAL'])
MQTT_TOPIC = aws_settings['MQTT_TOPIC']
MQTT_HOST = aws_settings['MQTT_HOST']
CA_ROOT_CERT_FILE = aws_settings['CA_ROOT_CERT_FILE']
THING_CERT_FILE = aws_settings['THING_CERT_FILE']
THING_PRIVATE_KEY = aws_settings['THING_PRIVATE_KEY']

# Read DB Settings from settings.ini file
db_settings = get_Settings('DB_SETTINGS')

DB_HOST = db_settings['DB_HOST']
DB_PORT = db_settings['DB_PORT']
DB_NAME = db_settings['DB_NAME']
DB_USER = db_settings['DB_USER']
#DB_PASSWORD = db_settings['DB_PASSWORD']
#=============================================================



#=============================================================
#===== SAVE DATA IN DATABASE ======
#=============================================================
# Open DB Connection
try:
	print "Trying to open DB Connection (DB HOST: " + str(DB_HOST) + ")..."
	time.sleep(45)
	db_connection = Sensor_DB_Class(DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME)
except:
	print ("Failed to connect to the DB. Please check the DB IP, Port and Password.")
	exit(1)


# Save Sensor Data in the Database
def save_sensor_data(json_payload):
	try:
		db_connection.insert_into_database(json_payload)
	except:
		print "Error while saving sensor data into the DB"
#=============================================================



#=============================================================
#===== MQTT - AWS IOT CORE ======
#=============================================================

# Initiate MQTT Client
mqttc = mqtt.Client()

# This function will be invoked every time,
# a new message arrives for the subscribed topic 
def on_message(mosq, obj, msg):
	#print "Topic: " + str(msg.topic)
	#print "QoS: " + str(msg.qos)
	#print "Payload: " + str(msg.payload)
	if msg.payload:
		try:
			print (msg.payload)
			# If it is a valid Sensor Data json (Check if all the required Json Keys are in Json payload)
			if all (k in (json.loads(msg.payload)) for k in ('SensorID','Location','DateTime','Temperature','Humidity')):
				save_sensor_data(msg.payload)
		except:
			pass

def on_subscribe(client, userdata, mid, granted_qos):
	print "Subscribed to mqtt topic: " + str(MQTT_TOPIC)

# This function will be triggered on successful MQTT connection
def on_connect(client, userdata, flags, rc):
	print ("Successfully Connected to AWS IoT Core.")
	print ("Trying to sbscribe to topic: " + str(MQTT_TOPIC))
	mqttc.subscribe(MQTT_TOPIC, 0)


# Connection Clean-up
def close_connection():
	print ('inside at-exit function...')
	# Close DB Connection.
	try:
		# Connection will be closed gracefully in the Sensor_DB_Class destructor
		del db_connection
	except:
		print "Unable to close DB Connection"
	# Close MQTT session
	try:
		mqttc.disconnect()
		del mqttc
	except:
		pass

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Configure TLS Set
print ("Trying to create MQTT TLS Set for authentication...")
mqttc.tls_set(CA_ROOT_CERT_FILE, certfile=THING_CERT_FILE, keyfile=THING_PRIVATE_KEY, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

# Connect with MQTT Broker
print ("Trying to connected to AWS IoT Core...")
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)	

# Register at-exit function to clean-up the connections
atexit.register(close_connection)

# Continue monitoring the incoming messages for subscribed topic
mqttc.loop_forever()
#=============================================================
