#!/usr/bin/env python

import calendar
import datetime
import sqlite3

db_source_file = 'CFGP.db'
db_dest_file = 'db.sqlite3'


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

source_db = create_connection(db_source_file)
dest_db = create_connection(db_dest_file)

def migrate_data(conn, fields):
    sql = ''' INSERT INTO WOD(workout, date, coach, url)            
                VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, fields)
    conn.commit()
    return cur.lastrowid

def get_data(conn):
    sql = """SELECT workout, date, coach, url from WOD"""

    try:
        # Execute the SQL command
        cur = conn.cursor()
        cur.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cur.fetchall()
        return results
    except sqlite3.Error as e:
        print(e)
workout_data = get_data(source_db)

for row in workout_data:
    url = row[3].replace("crossfitgreenpoint","greenpointathletics")
    workout = (row[0], row[1], row[2], url)
    print(migrate_data(dest_db,workout))



