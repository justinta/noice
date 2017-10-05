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
        conn.row_factory = sqlite3.Row

        c = conn.cursor()
        c.execute(sql)
        if 'SELECT' in sql:
            return c.fetchone()

        conn.commit()
        conn.close()

    def _create_table(self):
        """
        creates note table
        """
        sql = '''CREATE TABLE notes (
                    id  INTEGER PRIMARY KEY AUTOINCREMENT,
                    title           TEXT    NOT NULL, 
                    note            TEXT    NOT NULL)'''
        try:
            self._connect(sql)
        except sqlite3.OperationalError as e:
            pass

    def select_note(self, title):
        """
        Get a note based on a given title
        """
        sql = 'SELECT note FROM notes where title="{0}"'.format(title)
        note = self._connect(sql)
        return note[0]

    def select_all(self):
        """
        Get all the titles for given notes
        """
        sql = 'SELECT * from notes'
        all_notes = self._connect(sql)
        return all_notes

    def create_note(self, title, note):
        """
        Create a note
        """
        sql = 'INSERT INTO notes (title, note) VALUES ("{0}", "{1}")'.format(title, note)
        self._connect(sql)
        return 'Note created'
