import json
import requests
import json
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template('home.html')


@app.route("/dashboard/<city_name>", methods=['GET'])
def iot_dashboard(city_name):

	selected_city = city_name
	cities_list = []
	sensor_data_dict = {}
	
	r = requests.get('http://192.168.36.154:5050/sensor_data/' + str(city_name))
	if r.status_code == 200:
		sensor_data_dict = json.loads(r.text)
		
	else:
		print (r.status_code)
		print ("Failed to retrieve sensor data over REST API")


	r = requests.get('http://192.168.36.154:5050/cities')
	if r.status_code == 200:
		city_dict = json.loads(r.text)
		cities_list = city_dict ['cities']
		if (selected_city == 'city') and (len(cities_list) > 0):
			selected_city = cities_list[0]

		
	else:
		print (r.status_code)
		print ("Failed to retrieve cities data over REST API")

	return render_template('dashboard.html', sensor_data_dict=sensor_data_dict, cities_list=cities_list, selected_city=selected_city)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5061, debug=True)
