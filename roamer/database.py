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
    conn.execute("""
                   CREATE TABLE IF NOT EXISTS entries (
                      id INTEGER PRIMARY KEY,
                      digest TEXT,
                      name TEXT,
                      path TEXT,
                      trash BOOLEAN NOT NULL CHECK (trash IN (0,1)),
                      version INTEGER,
                      CONSTRAINT unique_digest UNIQUE (digest),
                      CONSTRAINT unique_full_path UNIQUE (name, path)
                    )
               """)
    conn.commit()
