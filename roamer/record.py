"""
Saves entries and their digests onto disk so they can be used in later sessions.
"""
from roamer.entry import Entry
from roamer.constant import ROAMER_DATA_PATH
from roamer.directory import Directory
from roamer.database import connection

def load(filter_dir=None, trash=False):
    dictionary = {}
    conn = connection()
    cursor = conn.cursor()
    query = 'SELECT * FROM entries WHERE trash = ? AND path != ?'
    for row in cursor.execute(query, (trash, str(filter_dir))):
        entry = Entry(row['name'], Directory(row['path'], []), row['digest'])
        dictionary[row['digest']] = entry
    return dictionary

def add_dir(directory):
    conn = connection()
    query = 'DELETE FROM entries WHERE path = ?'
    conn.execute(query, (str(directory),))
    for entry in directory.entries.values():
        check_conflict(conn, entry.digest, entry.name, entry.directory.path, False)
        conn.execute("""
                       INSERT OR REPLACE INTO entries(digest, name, path, trash)
                       VALUES ( ?, ?, ?, ? )
                     """, (entry.digest, entry.name, entry.directory.path, False))
    conn.commit()

def add_trash(digest, name, directory):
    conn = connection()
    check_conflict(conn, digest, name, directory, True)
    conn.execute("""
                   INSERT OR REPLACE INTO entries(digest, name, path, trash)
                   VALUES ( ?, ?, ?, ? )
                 """, (digest, name, directory, True))
    conn.commit()

def check_conflict(conn, digest, name, path, is_trash):
    query = 'SELECT * from entries where digest = ? AND trash = ?'
    cursor = conn.cursor()
    cursor.execute(query, (digest, is_trash))
    result = cursor.fetchone()
    if not result:
        return False
    if result['name'] == name and result['path'] == path and not is_trash:
        return False
    raise DigesetCollision('Hash collision.  Try deleting: %s' % ROAMER_DATA_PATH)

class DigesetCollision(Exception):
    pass
