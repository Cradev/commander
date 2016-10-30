#!/usr/bin/env python

import sqlite3

class DBManager:

    def __init__(self, dbname):
        global conn, curs
        conn = sqlite3.connect(dbname)
        curs = conn.cursor()

    def install(self):
        '''Add the tables/rows to the database. '''
        curs.execute('''CREATE TABLE commands 
                        (id INTEGER PRIMARY KEY, title TEXT, command TEXT)''')
        conn.commit()

    def connect(self):
        ''' Test whether we can store something in the database'''
        try:
            curs.execute('SELECT * FROM commands')
        except:
            self.createDB()

    def add_record(self, data):
        ''' Add a record to the database. '''
        curs.execute('INSERT INTO commands VALUES (NULL, ?, ?)', data)
        try:
            conn.commit()
            print("The command has been added to the database.")
        except:
            print("The command couldn't be added.")

    def del_record_by_id(self, id):
        ''' Delete a record from the database. '''
        curs.execute('DELETE FROM commands WHERE id=?', (id,))

        try:
            conn.commit()
            print("Successfully deleted record with ID: {0}").format(id)
        except:
            print("Could not delete record")

    def show_record_by_id(self, id):
        ''' Get a record based on the defined ID. '''
        curs.execute('SELECT * FROM commands WHERE id=?', (id,))
        conn.commit()

        return curs.fetchone()

    def show_all_records(self):
        ''' Returns all stored commands in the database. '''
        try:
            curs.execute('SELECT * FROM commands')
            conn.execute()
            return curs.fetch()
        except:
            print("No results were found.")


