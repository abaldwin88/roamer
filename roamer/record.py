"""
Saves entries and their digests onto disk so they can be used in later sessions.
"""
from roamer.constant import ROAMER_DATA_PATH
from roamer.database import connection

def load(filter_dir=None, trash=False):
    conn = connection()
    cursor = conn.cursor()
    query = 'SELECT * FROM entries WHERE trash = ? AND path != ?'
    cursor.execute(query, (trash, str(filter_dir)))
    return cursor.fetchall()

def add_dir(directory):
    conn = connection()
    query = 'DELETE FROM entries WHERE path = ?'
    conn.execute(query, (str(directory),))
    for entry in directory.entries.values():
        check_conflict(conn, entry.digest, entry.name, entry.directory.path, False)
        query = 'INSERT OR REPLACE INTO entries(digest, name, path, trash)' \
                'VALUES ( ?, ?, ?, ? )'
        conn.execute(query, (entry.digest, entry.name, entry.directory.path, False))
    conn.commit()

def add_trash(digest, name, directory):
    conn = connection()
    check_conflict(conn, digest, name, directory, True)
    query = 'INSERT OR REPLACE INTO entries(digest, name, path, trash) VALUES ( ?, ?, ?, ? )'
    conn.execute(query, (digest, name, directory, True))
    conn.commit()

def check_conflict(conn, digest, name, path, is_trash):
    query = 'SELECT * FROM entries WHERE digest = ? AND trash = ?'
    cursor = conn.cursor()
    cursor.execute(query, (digest, is_trash))
    result = cursor.fetchone()
    if not result:
        return False
    if result['name'] == name and result['path'] == path and not is_trash:
        return False
    raise DigesetCollision('Hash collision.  Try deleting: %s' % ROAMER_DATA_PATH)

def get_version(path, name):
    conn = connection()
    cursor = conn.cursor()
    query = 'SELECT version FROM modifications WHERE path = ? AND name = ?'
    cursor.execute(query, (path, name))
    result = cursor.fetchone()
    if not result:
        return None
    return result['version']

def set_version(path, name, version):
    conn = connection()
    query = 'INSERT OR REPLACE INTO modifications(path, name, version) VALUES ( ?, ?, ? )'
    conn.execute(query, (path, name, version))
    conn.commit()


class DigesetCollision(Exception):
    pass
