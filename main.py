import requests
import sqlite3


connection = sqlite3.connect('KFC_database.db')
cursor = connection.cursor()

url = 'https://api.prod.digital.uni.rest/api/store/v2/store.get_restaurants?showClosed=true'

response = requests.get(url)

if response.status_code != 200:
    raise requests.HTTPError

restaurants = response.json()['searchResults']
for restarant in restaurants:
    restarant_data = restarant['storePublic']
    title = restarant_data['title']['ru']
    contacts = restarant_data['contacts']
    city = contacts['city']['ru']
    coorditates = contacts['coordinates']['geometry']['coordinates']

    opening_hours = restarant_data['openingHours']['regular']
    opening_time = opening_hours['startTimeLocal']
    closing_time = opening_hours['endTimeLocal']

    breakfast_hours = restarant_data['menues'][0]['availability']['regular']
    start_breakfast_time = breakfast_hours['startTimeLocal']
    end_breakfast_time = breakfast_hours['endTimeLocal']

    row = (title, city, coorditates[0], coorditates[1], opening_time, closing_time, start_breakfast_time, end_breakfast_time)
    cursor.execute(
        'INSERT INTO restaurants (title, city, lat, lon, opening_time, closing_time, start_breakfast_time, end_breakfast_time)\
              VALUES (?, ?, ?, ?, ?, ?, ?, ?)', row
    )

connection.commit()
connection.close()