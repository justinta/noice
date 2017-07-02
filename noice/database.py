# -*- coding: utf-8 -*-
"""
Database stuff
"""
import sqlite3


class NoiceDB():
    def __init__(self):
        pass

    def _connect(self, sql):
        """
        connects to sqlite3 database
        """
        conn = sqlite3.connect('noice.db')

        c = conn.cursor()
        c.execute(sql)

        conn.commit()
        conn.close()

    def _create_table(self):
        """
        creates note table
        """
        sql = 'CREATE TABLE notes (title, note)'
        try:
            self._connect(sql)
        except sqlite3.OperationalError:
            print('table already created')

    def select_note(self, title):
        """
        Get a note based on a given title
        """
        sql = 'SELECT * FROM notes where title={0}'.format(title)
        self._connect(sql)

    def create_note(self, title, note):
        """
        Create a note
        """
        sql = 'INSERT INTO notes VALUES ("{0}", "{1}")'.format(title, note)
        self._connect(sql)
        return 'Note created'
