import requests
import sqlite3
from DB_manager import prepare_db


def get_restaurants_from_API() -> dict:
    url = 'https://api.prod.digital.uni.rest/api/store/v2/store.get_restaurants?showClosed=false'

    response = requests.get(url)
    if response.status_code != 200:
        raise requests.HTTPError
    
    return response.json()['searchResults']


def get_restaurant_data(restaurant) -> tuple:
    restaurant_data = restaurant['storePublic']
    title = restaurant_data['title']['ru']
    contacts = restaurant_data['contacts']
    city = contacts['city']['ru']
    coorditates = contacts['coordinates']['geometry']['coordinates']

    opening_hours = restaurant_data['openingHours']['regular']
    opening_time = opening_hours['startTimeLocal']
    closing_time = opening_hours['endTimeLocal']

    breakfast_hours = restaurant_data['menues'][0]['availability']['regular']
    start_breakfast_time = breakfast_hours['startTimeLocal']
    end_breakfast_time = breakfast_hours['endTimeLocal']

    return (title, city, coorditates[0], coorditates[1], opening_time, closing_time, start_breakfast_time, end_breakfast_time)
    

def main():
    connection = sqlite3.connect('KFC_database.db')
    cursor = connection.cursor()
    prepare_db(cursor)

    restaurants: dict = get_restaurants_from_API()
    for restaurant in restaurants:
        row = get_restaurant_data(restaurant)
        cursor.execute(
            'INSERT INTO restaurants (title, city, lat, lon, opening_time, closing_time, start_breakfast_time, end_breakfast_time)\
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)', row
        )

    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()