import requests
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import geopy.distance

app = Flask(__name__)
CORS(app)

@app.route('/v2/all')
def testing():
    nature_url = 'https://citynature.eu/api/wp/v2/places?cityid=5'

    nature_data = requests.get(nature_url).json()

    # Function for getting the weather at a certain location
    def get_weather(latitude, longitude):
        url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + \
            str(latitude)+'&lon='+str(longitude) + \
            '&APPID=f2977c0caa82f7d12782acc03ed6f31d&units=metric'
        weather_data = requests.get(url).json()
        return weather_data

    list_of_objects = []
    for i in nature_data:
        coordinates = i['routes']['features'][0]['geometry']['coordinates'][0]
        routes = i['routes']['features']
        for route in i['routes']['features']:
            distance = 0
            for coordinate_1, coordinate_2 in zip(
                route["geometry"]["coordinates"][:-1], route["geometry"]["coordinates"][1:]
            ):
                distance += geopy.distance.distance(coordinate_1, coordinate_2).km
            route['length'] = distance
        points = i['points']
        lat = coordinates[1] # We use these to get coordinates for the weather API
        lon = coordinates[0]
        weather_data = get_weather(lat, lon)
        weather_state = weather_data['weather'][0]['main']
        weather_detail = weather_data['weather'][0]['description']
        weather_temp = weather_data['main']['temp']
        wind_speed = weather_data['wind']['speed']
        wind_direction = weather_data['wind']['deg']
        json_object = {'locationName': i['title'],
                'latitude': lat,
                'longitude': lon,
                'routes': routes,
                'points': points,
                'weather': {'weather': weather_state,
                            'description': weather_detail,
                            'temperature': weather_temp,
                            'windSpeed': wind_speed,
                            'windDirection': wind_direction}

                }
        list_of_objects.append(json_object)

    return jsonify({'response': list_of_objects})

if __name__ == '__main__':
    app.run(debug=True)
