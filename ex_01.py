import sqlite3

conn = sqlite3.connect('nobelPrizes.db')

cursor = conn.cursor()

create_prize_table_query = '''
CREATE TABLE IF NOT EXISTS prize (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    laureate_id INTEGER,
    category_id INTEGER,
    year INTEGER,
    affiliation_id INTEGER,
    FOREIGN KEY (laureate_id) REFERENCES person(id),
    FOREIGN KEY (category_id) REFERENCES category(id),
    FOREIGN KEY (affiliation_id) REFERENCES country(id)
);
'''

create_person_table_query = '''
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    gender VARCHAR,
    born DATE,
    died DATE,
    bornCountry_id INTEGER,
    diedCountry_id INTEGER,
    FOREIGN KEY (bornCountry_id) REFERENCES country(id),
    FOREIGN KEY (diedCountry_id) REFERENCES country(id)
);
'''

create_category_table_query = '''
CREATE TABLE IF NOT EXISTS category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL UNIQUE
);
'''

create_country_table_query = '''
CREATE TABLE IF NOT EXISTS country (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    code VARCHAR
);
'''

cursor.execute(create_country_table_query)
cursor.execute(create_category_table_query)
cursor.execute(create_person_table_query)
cursor.execute(create_prize_table_query)


# Commit the changes and close the cursor and connection
conn.commit()
conn.close()