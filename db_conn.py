import sqlite3

class DB:
    @staticmethod
    def initialize():
        with sqlite3.connect('notes.db') as conn:
            cursor = conn.cursor()
            with open('setup.sql', 'r') as setup_file:
                setup_query = setup_file.read()
                cursor.executescript(setup_query)
