import datetime
import sqlite3
import json

# Initialize the database
conn = sqlite3.connect('nobelPrizes.db')

cursor = conn.cursor()
cursoranother = conn.cursor()


def add_persons():
    with open('D-POO-300_07_nobelLaureates.json', 'r') as myjsonfilelaureates:
        data = json.load(myjsonfilelaureates)
        born_country_code = 0
        dead_country_code = 0

        for element in data['laureates']:

            # Get the born id country
            try:
                borncountryquery = "SELECT id FROM country WHERE (name) is ?"
                cursor.execute(borncountryquery, (element['bornCountry'],))
                rows = cursor.fetchall()
                for row in rows:
                    born_country_code = row[0]
            except:
                born_country_code = 0
            # Get the dead id country
            try:
                borncountryquery = "SELECT id FROM country WHERE (name) is ?"
                cursoranother.execute(borncountryquery, (element['deadCountry'],))
                rowsdead = cursoranother.fetchall()
                for data in rowsdead:
                    dead_country_code = data[0]
            except:
                dead_country_code = 0

            insert_query = "INSERT INTO person (name, gender, born, died, bornCountry_id, diedCountry_id) VALUES (?, ?, ?, ?, ?, ?)"

            try:
                cursor.execute(insert_query, (element['firstname'] + ' ' + element['surname'], element['gender'],
                                              datetime.datetime(int(element['born'].split('-')[0]),
                                                                int(element['born'].split('-')[1]),
                                                                int(element['born'].split('-')[2])),
                                              datetime.datetime(int(element['died'].split('-')[0]),
                                                                int(element['died'].split('-')[1]),
                                                                int(element['died'].split('-')[2])), born_country_code,
                                              dead_country_code))
            except:
                try:
                    cursor.execute(insert_query, (element['firstname'], element['gender'],
                                                  datetime.datetime(int(element['born'].split('-')[0]),
                                                                    int(element['born'].split('-')[1]),
                                                                    int(element['born'].split('-')[2])),
                                                  datetime.datetime(int(element['died'].split('-')[0]),
                                                                    int(element['died'].split('-')[1]),
                                                                    int(element['died'].split('-')[2])),
                                                  born_country_code, dead_country_code))
                except:
                    cursor.execute(insert_query, (element['firstname'], element['gender'],
                                                  datetime.datetime(2000, 1, 1),
                                                  datetime.datetime(2000, 1, 1), born_country_code, dead_country_code))

                conn.commit()


if __name__ == '__main__':
    add_persons()
