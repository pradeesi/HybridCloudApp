import mysql.connector as mariadb
import json
import datetime
import time

class Sensor_DB_Class:

	# Constructor
	def __init__(self, db_host, db_port, db_user, db_password, db_name):
		self.db_host = db_host
		self.db_port = db_port
		self.db_user = db_user
		self.db_password = db_password
		self.db_name = db_name
		# Initialize DB - If not exists
		self.initialize_db()
		# Open DB Connection
		self.open_db_connection()

	# Create Database and Table (If doesn't exist)
	def initialize_db(self):
		try:
			# Connect to DB
			mariadb_connection = mariadb.connect(host=self.db_host, port=self.db_port, user=self.db_user, password=self.db_password)
			# Initialize cursor object
			cursor = mariadb_connection.cursor()
			# Create DB if it doesn't exists
			cursor.execute('create database if not exists ' + self.db_name + ';')
			# Create Sensor Data Table
			cursor.execute('create table if not exists ' + self.db_name + '.sensor_data (Rec_ID int NOT NULL AUTO_INCREMENT PRIMARY KEY, Sensor_ID INT, Location varchar(255), Sensor_DateTime datetime, DB_DateTime datetime, Temperature DECIMAL(5,2), Humidity DECIMAL(5,2))')
			# Commit the changes
			mariadb_connection.commit()
			# Close Cursor
			cursor.close()
			# Close the DB Connection
			mariadb_connection.close()
		except mariadb.Error as error:
			print("Error: {}".format(error))

	# Open a DB Connection
	def open_db_connection(self):
		try:
			# Open DB connection
			mariadb_connection = mariadb.connect(host=self.db_host, port=self.db_port, user=self.db_user, password=self.db_password, database=self.db_name)
			# Initialize cursor object
			cursor = mariadb_connection.cursor()
			# Set Automcommit ON to avoid metadata-locks
			# Details at the following link -
			# https://mariadb.com/resources/blog/every-select-from-your-python-program-may-acquire-a-metadata-lock/
			cursor.execute('SET AUTOCOMMIT=1')

			self.mariadb_connection = mariadb_connection
			self.cursor = cursor
		except mariadb.Error as error:
			print("Error: {}".format(error))

	# Close DB Connection
	def close_db_connection(self):
		try:
			try:
				# commit any pending changes
				self.mariadb_connection.commit()
			except mariadb.Error as error:
				print("Error: {}".format(error))
			try:
				# Close Cursor
				self.cursor.close()
			except mariadb.Error as error:
				print("Error: {}".format(error))
			try:
				# close the connection
				self.mariadb_connection.close()
			except mariadb.Error as error:
				print("Error: {}".format(error))
		except:
			print "Error while closing the DB connection"

		# Handle connection time-out cases with the DB
	def execute_sql_query(self, sql_query):
		# Try to execute the query
		try:
			cursor = self.cursor
			cursor.execute(sql_query)
		except (AttributeError, mariadb.OperationalError):
			# In case of Connection Time-out, reopen the connection and try again
			try:
				# Re-open connection and execute the query.
				self.open_db_connection()
				cursor = self.cursor
				cursor.execute(sql_query)
			except mariadb.Error as error:
				print("Error: {}".format(error))
		# Return the cursor
		return cursor


	# Save Sensor Data into the Database
	def insert_into_database(self, json_payload):
		# Try to insert data into the database
		try:
			# Parse Data
			sensor_data = json.loads(json_payload)
			sensor_id = sensor_data['SensorID']
			location = sensor_data['Location']
			sensor_datetime = sensor_data['DateTime']
			db_datetime = str(datetime.datetime.utcnow())
			temperature = float("{0:.2f}".format(sensor_data['Temperature']))
			humidity =  float("{0:.2f}".format(sensor_data['Humidity']))

			self.cursor.execute('INSERT INTO sensor_data (Sensor_ID, Location, Sensor_DateTime, DB_DateTime, Temperature, Humidity) VALUES (%s, %s, %s, %s, %s, %s)', (sensor_id, location, sensor_datetime, db_datetime, temperature, humidity))
			self.mariadb_connection.commit()
		except (AttributeError, mariadb.OperationalError):
			# In case of Connection Time-out, reopen the connection and try again
			try:
				# Re-open connection and execute the query.
				self.open_db_connection()
				self.cursor.execute('INSERT INTO sensor_data (Sensor_ID, Location, Sensor_DateTime, DB_DateTime, Temperature, Humidity) VALUES (%s, %s, %s, %s, %s, %s)', (sensor_id, location, sensor_datetime, db_datetime, temperature, humidity))
				self.mariadb_connection.commit()
			except mariadb.Error as error:
				print("Error: {}".format(error))
		except:
			print "Error while trying to insert data into the databse"
		return


	# Destroctor
	def __del__(self):
		# Close DB connection
		self.close_db_connection()

