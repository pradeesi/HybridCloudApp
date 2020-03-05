import ConfigParser
import json
from flask import Flask
from mariadb_con_api_service import Sensor_DB_Class
import time
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

# Read DB Settings from settings.ini file
db_settings = get_Settings('DB_SETTINGS')

DB_HOST = db_settings['DB_HOST']
DB_PORT = db_settings['DB_PORT']
DB_NAME = db_settings['DB_NAME']
DB_USER = db_settings['DB_USER']
#DB_PASSWORD = db_settings['DB_PASSWORD']


# Read App Settings
app_settings = get_Settings('APP_SETTINGS')

APP_PORT = app_settings['HTTP_PORT']

#=============================================================


#=============================================================
#===== QUERY DATABASE ======
#=============================================================
# Open DB Connection
print ("Trying to connect to DB...")
time.sleep(10)
db_connection = Sensor_DB_Class(DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME)


def read_cities():
	
	cursor = db_connection.execute_sql_query('select distinct Location from sensor_data;')
	
	cities_list = []
	for city in cursor.fetchall():
		cities_list.append(str(city[0]).encode('ascii', 'ignore'))

	cities_dict = {} 
	cities_dict['cities'] = cities_list

	cities_json = json.dumps(cities_dict)
	
	return cities_json


def read_temperature():

	cursor = db_connection.execute_sql_query("""
		SELECT
		  Location,
		  CONCAT(
		    '[',
		      GROUP_CONCAT(
		        JSON_OBJECT(
		          'Temp', Temperature,
		          'Time', DATE_FORMAT(Sensor_DateTime,"%H:%i:%s")
		        )
		      ),
		    ']'
		  ) AS list
		FROM
		  sensor_data
		GROUP BY
		  Location;
		""")
	
	temperature_dict = {}
	
	for item in cursor.fetchall():
		temperature_dict[item[0].encode('ascii', 'ignore')] = json.loads(item[1].encode('ascii', 'ignore'))
	
	temperature_json = json.dumps(temperature_dict)
	return temperature_json


def read_humidity():

	cursor = db_connection.execute_sql_query("""
		SELECT
		  Location,
		  CONCAT(
		    '[',
		      GROUP_CONCAT(
		        JSON_OBJECT(
		          'Humi', Humidity,
		          'Time', Sensor_DateTime
		        )
		      ),
		    ']'
		  ) AS list
		FROM
		  sensor_data
		GROUP BY
		  Location;
		""")

	humidity_dict = {}
	
	for item in cursor.fetchall():
		humidity_dict[item[0].encode('ascii', 'ignore')] = json.loads(item[1].encode('ascii', 'ignore'))

	humidity_json = json.dumps(humidity_dict)
	return humidity_json


def read_sensor_data(city_name):

	if city_name == 'city':
		city_dict = json.loads(read_cities())
		cities_list = city_dict ['cities']
		if len(cities_list) > 0:
			city_name = cities_list[0]

	if city_name == 'city':
		cursor = db_connection.execute_sql_query("""
			SELECT
			  Location,
			  CONCAT(
			    '[',
			      GROUP_CONCAT(
			        JSON_OBJECT(
			          'Temperature', Temperature,
			          'Humidity', Humidity,
			          'Time', DATE_FORMAT(Sensor_DateTime,"%H:%i:%s")
			        )
			      ),
			    ']'
			  ) AS list
			FROM
			  sensor_data
			GROUP BY
			  Location
			ORDER BY Rec_ID;
			""")
	else:
		cursor = db_connection.execute_sql_query("""
			SELECT
			  Location,
			  CONCAT(
			    '[',
			      GROUP_CONCAT(
			        JSON_OBJECT(
			          'Temperature', Temperature,
			          'Humidity', Humidity,
			          'Time', DATE_FORMAT(Sensor_DateTime,"%H:%i:%s")
			        )
			      ),
			    ']'
			  ) AS list
			FROM
			  sensor_data WHERE Location = '""" + str(city_name) + 
			"""' GROUP BY Location 
			  ORDER BY Rec_ID;
			""")

	sensor_data_dict = {}
	
	for item in cursor.fetchall():
		#City		
		city_data_dict = {}
		humidity_list = []
		temperature_list = []
		time_list = []
		# Create Lists of Humidity, Temperature and Time
		for data in json.loads(item[1]):
			humidity_list.append(data['Humidity'])
			temperature_list.append(data['Temperature'])
			time_list.append(data['Time'])
		# Add Lists to City Dictionary
		city_data_dict['Humidity'] = humidity_list
		city_data_dict['Temperature'] = temperature_list
		city_data_dict['Time'] = time_list

		#Add City Dictionaty to sensor_data_dict
		sensor_data_dict[item[0]] = city_data_dict

	sensor_data_json = json.dumps(sensor_data_dict)
	return sensor_data_json

#=============================================================



#=============================================================
#===== FLAST REST APIs ======
#=============================================================

app = Flask(__name__)

@app.route("/")
def welcome():
	return "Welcome to the API Service...!"


@app.route("/cities", methods=['GET'])
def get_cities():
	return read_cities()


@app.route("/temperature", methods=['GET'])
def get_temperature():
	return read_temperature()


@app.route("/humidity", methods=['GET'])
def get_humidity():
	return read_humidity()


@app.route("/sensor_data/<city_name>", methods=['GET'])
def get_sensor_data(city_name):
	return read_sensor_data(city_name)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=APP_PORT)
	
#=============================================================

