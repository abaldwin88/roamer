"""
Saves entries and their digests onto disk so they can be used in later sessions.
"""
from roamer.entry import Entry
from roamer.constant import ROAMER_DATA_PATH
from roamer.directory import Directory
from roamer.database import connection

class Record(object):
    def __init__(self, filter_directory=None):
        self._filter_directory = filter_directory
        self.entries = self._load(trash=False)
        self.trash_entries = self._load(trash=True)

    def _load(self, trash):
        dictionary = {}
        conn = connection()
        cursor = conn.cursor()
        query = 'SELECT * FROM entries WHERE trash = ? AND path != ?'
        for row in cursor.execute(query, (trash, str(self._filter_directory))):
            entry = Entry(row['name'], Directory(row['path'], []), row['digest'])
            dictionary[row['digest']] = entry
        return dictionary

    def add_dir(self, directory):
        conn = connection()
        entries = {}
        for entry in self.entries.values():
            if entry.directory != directory:
                assign(entries, entry.digest, entry.name, entry.directory.path)
        for entry in directory.entries.values():
            assign(entries, entry.digest, entry.name, entry.directory.path)

        for digest, entry in entries.items():
            conn.execute("""
                           INSERT OR REPLACE INTO entries(digest, name, path, trash)
                           VALUES ( ?, ?, ?, ? )
                         """, (digest, entry['name'], entry['directory'], False))
        conn.commit()

    def add_trash(self, digest, name, directory):
        conn = connection()
        entries = {}
        for entry in self.trash_entries.values():
            assign(entries, entry.digest, entry.name, entry.directory.path)
        assign(entries, digest, name, directory)

        for entry_digest, entry in entries.items():
            conn.execute("""
                           INSERT OR REPLACE INTO entries(digest, name, path, trash)
                           VALUES ( ?, ?, ?, ? )
                         """, (entry_digest, entry['name'], entry['directory'], True))
        conn.commit()

def assign(entries, digest, name, directory):
    if digest in entries:
        raise DigesetCollision('Hash collision.  Try deleting: %s' % ROAMER_DATA_PATH)
    entries[digest] = {'name': name, 'directory': directory}

class DigesetCollision(Exception):
    pass
