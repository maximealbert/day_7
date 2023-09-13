import sqlite3
import json

conn = sqlite3.connect('nobelPrizes.db')

cursor = conn.cursor()

def add_category():
    with open('D-POO-300_07_nobelPrizes.json', 'r') as myjsonfile:
        data = json.load(myjsonfile)
        category_list = []

        for element in data['prizes']:
            category_list = category_list + [element['category']]

        category_list = list(set(category_list))

        for element in sorted(category_list):
            insert_query = "INSERT INTO category (name) VALUES (?)"
            try:
                cursor.execute(insert_query, (element,))
                conn.commit()
            except:
                print('Cannot add value that is already in the database')


def add_country():

    with open('D-POO-300_07_nobelCountries.json', 'r') as myjsonfilecountry:
        data = json.load(myjsonfilecountry)
        country_list = []
        for element in data['countries']:
            try:
                country_list = country_list + [(element['name'], element['code'])]
            except:
                country_list = country_list + [(element['name'], 'N/A')]
        sorted_list = sorted(country_list, key=lambda x: x[0])

        print(sorted_list[0][1])

        for element in sorted_list:
            insert_query = "INSERT INTO country (name, code) VALUES (?, ?)"
            try:
                cursor.execute(insert_query, (element[0], element[1]))
                conn.commit()
            except:
                print('Cannot add value that is already in the database')



if __name__ == '__main__':
    add_country()
