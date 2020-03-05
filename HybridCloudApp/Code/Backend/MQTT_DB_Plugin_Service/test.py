import paho.mqtt.client as mqtt
import ssl
import time
import json
import datetime
import ConfigParser
import atexit
import os


MQTT_PORT = 8883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = 'sensor_data'
MQTT_HOST = 'a1w96bpaqp1dlq-ats.iot.us-east-2.amazonaws.com'
CA_ROOT_CERT_FILE = 'AmazonRootCA.crt'
THING_CERT_FILE = 'daed173360-certificate.pem.crt'
THING_PRIVATE_KEY = 'daed173360-private.pem.key'


mqttc = mqtt.Client()


def on_message(mosq, obj, msg):
	print "Topic: " + str(msg.topic)
	print "QoS: " + str(msg.qos)
	print "Payload: " + str(msg.payload)


def on_subscribe(client, userdata, mid, granted_qos):
	print "Subscribed to mqtt topic: " + str(MQTT_TOPIC)

def on_connect(client, userdata, flags, rc):
	print ("Successfully Connected to AWS IoT Core.")
	print ("Trying to sbscribe to topic: " + str(MQTT_TOPIC))
	mqttc.subscribe(MQTT_TOPIC, 0)


mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Configure TLS Set
print ("Trying to create MQTT TLS Set for authentication...")
mqttc.tls_set(CA_ROOT_CERT_FILE, certfile=THING_CERT_FILE, keyfile=THING_PRIVATE_KEY, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

# Connect with MQTT Broker
print ("Trying to connect to AWS IoT Core...")
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)	

# Continue monitoring the incoming messages for subscribed topic
mqttc.loop_forever()
