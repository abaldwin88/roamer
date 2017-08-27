"""
Handle connection and initialization of sqlite3 database
"""
import sqlite3
from roamer.constant import ROAMER_DATABASE

DB = sqlite3.connect(ROAMER_DATABASE)

def connection():
    conn = sqlite3.connect(ROAMER_DATABASE)
    conn.row_factory = sqlite3.Row
    conn.text_factory = str
    return conn

def db_init():
    conn = connection()
    query = """
               CREATE TABLE IF NOT EXISTS entries (
                  id INTEGER PRIMARY KEY,
                  digest TEXT,
                  name TEXT,
                  path TEXT,
                  trash BOOLEAN NOT NULL CHECK (trash IN (0,1)),
                  CONSTRAINT unique_digest UNIQUE (digest),
                  CONSTRAINT unique_full_path UNIQUE (name, path)
               )
            """
    conn.execute(query)
    query = """
            CREATE TABLE IF NOT EXISTS modifications (
              id INTEGER PRIMARY KEY,
              name TEXT,
              path TEXT,
              version INTEGER,
              CONSTRAINT unique_full_path UNIQUE (name, path)
            )
            """
    conn.execute(query)
    conn.commit()
