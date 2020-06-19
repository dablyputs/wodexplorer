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

def migrate_coaches(conn, fields):
    sql = """INSERT INTO organizer_coach(name)
                VALUES(?)"""
    cur = conn.cursor()
    cur.execute(sql, fields)
    conn.commit()
    return cur.lastrowid

def migrate_wods(conn, fields):
    sql = """ INSERT INTO organizer_wod(workout, sched_date, orig_url, coach_link_id, gym_link_id)            
                VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, fields)
    conn.commit()
    return cur.lastrowid

def get_coaches(conn):
    sql = """SELECT DISTINCT coach from WOD"""

    try:
        # Execute the SQL command
        cur = conn.cursor()
        cur.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cur.fetchall()
        return results
    except sqlite3.Error as e:
        print(e)

def get_coach_id(conn,name):
    sql = "SELECT id FROM organizer_coach WHERE name='"+name+"'"
    print(sql)

    try:
        # Execute the SQL command
        cur = conn.cursor()
        cur.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cur.fetchall()
        return results
    except sqlite3.Error as e:
        print(e)

def get_wods(conn):
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

workout_data = get_wods(source_db)
coach_data = get_coaches(source_db)

for row in coach_data:
   coaches = (row[0],)
   print(migrate_coaches(dest_db,coaches))

for row in workout_data:
    url = row[3].replace("crossfitgreenpoint","greenpointathletics")
    coach_link = get_coach_id(dest_db, row[2])
    print(coach_link[0][0])
    workout = (row[0], row[1], url, coach_link[0][0], '1')
    print(migrate_wods(dest_db,workout))
