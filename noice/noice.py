# -*- coding: utf-8 -*-
"""
The main thing
"""
from __future__ import print_function

#python libs
import argparse

#noice libs
from database import NoiceDB


class Noice():
    """
    Noice.
    The start to something... Well, something.

    examples:
        noice get <title>
        noice create <title> <note>
    """
    def __init__(self):
        self.db = NoiceDB()

    def get(self, title):
        """
        Gets a note from the user
        """
        #TODO: make this work for real. need db or something
        notes = {'test': 'test note'}
        return notes[title]

    def create(self, title, new_note):
        """
        Gets a note from the user
        """

        self.db._create_table() # this needs to not be here
        print(self.db.create_note(title, new_note))


if __name__ == '__main__':
    notes = Noice()

    # gross...
    #TODO: make this not gross
    parser = argparse.ArgumentParser()
    parser.add_argument('--create', action='store_true', default=False, help='create a note')
    parser.add_argument('--title', default=None, help='title of note')
    parser.add_argument('--note', default=None, help='the note')
    parser.add_argument('--get', action='store_true', default=False, help='get a note')
    args = parser.parse_args()

    if args.create:
        notes.create(args.title, args.note)
    if args.get:
        notes.get(args.title)
