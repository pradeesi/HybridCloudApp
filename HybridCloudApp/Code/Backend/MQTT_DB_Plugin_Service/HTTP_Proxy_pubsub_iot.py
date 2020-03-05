import paho.mqtt.client as paho
import os
import socket
import ssl
from time import sleep
from random import uniform
import json
import socks

import logging
logging.basicConfig(level=logging.INFO)

# Refactored original source - https://github.com/mariocannistra/python-paho-mqtt-for-aws-iot

class PubSub(object):

    def __init__(self, listener = False, topic = "default"):
        print "init ..."
        self.connect = False
        self.listener = listener
        self.topic = topic
        self.logger = logging.getLogger(repr(self))

    def __on_connect(self, client, userdata, flags, rc):
        print "on_connect"
        self.connect = True
        
        if self.listener:
            self.mqttc.subscribe(self.topic)

        self.logger.debug("{0}".format(rc))

    def __on_message(self, client, userdata, msg):
        print "on_message"
        self.logger.info("{0}, {1} - {2}".format(userdata, msg.topic, msg.payload))

    def __on_log(self, client, userdata, level, buf):
        print "__on_log"
        self.logger.debug("{0}, {1}, {2}, {3}".format(client, userdata, level, buf))

    def bootstrap_mqtt(self):
        print "bootstrap_mqtt"

        self.mqttc = paho.Client()
        self.mqttc.on_connect = self.__on_connect
        self.mqttc.on_message = self.__on_message
        self.mqttc.on_log = self.__on_log

        awshost = "a4u41hr0i456b-ats.iot.us-west-2.amazonaws.com"
        awsport = 8883

        caPath = "./AmazonRootCA.crt" # Root certificate authority, comes from AWS with a long, long name
        certPath = "./d70185381e-certificate.pem.crt"
        keyPath = "./d70185381e-private.pem.key"

        self.mqttc.tls_set(caPath, 
            certfile=certPath, 
            keyfile=keyPath, 
            cert_reqs=ssl.CERT_REQUIRED, 
            tls_version=ssl.PROTOCOL_TLSv1_2, 
            ciphers=None)

        print "Connecting"
        # PROXY IP NEW 
        # 58.162.139.110 3128

        # PROXY_TYPE_HTTP or PROXY_TYPE_SOCKS5
        # sudo docker pull dlxneamtu/hybrid_cloud_backend:proxy_v2
        #socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, "10.96.164.50", 3128)
        socks.set_default_proxy(socks.PROXY_TYPE_HTTP, "58.162.139.110", 3128)
        socket.socket = socks.socksocket
        
        try:
             result_of_connection = self.mqttc.connect(awshost, awsport, keepalive=120)
             if result_of_connection == 0:
                print "Connected"
                self.connect = True
        except Exception as e:
            print 'Failed to upload to connect: '+ str(e)
    
        return self

    def start(self):
        self.mqttc.loop_start()

        while True:
            sleep(2)
            if self.connect == True:
                self.mqttc.publish(self.topic, json.dumps({"message": "Hello COMP680"}), qos=1)
            else:
                self.logger.debug("Attempting to connect.")

if __name__ == '__main__':
    
    PubSub(listener = True, topic = "sensor_data").bootstrap_mqtt().start()




