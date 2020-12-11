import sqlite3
import json
import urllib.request
import os
import hashlib
import mysql.connector
import ulid
from .alignment import alignment


# app initializer
def initialize():
    print('initialize')
    conn = sqlite3.connect(os.environ.get('INTERNAL_STORAGE'))

    # check and create query table
    conn.execute("""CREATE TABLE IF NOT EXISTS queries (
        id TEXT NOT NULL PRIMARY KEY,
        name TEXT NOT NULL,
        query TEXT NOT NULL,
        hashed_name TEXT NOT NULL
    )""")
    
    conn.execute("""CREATE INDEX IF NOT EXISTS IDX_queries_name ON queries(name)""")
    conn.execute("""CREATE UNIQUE INDEX IF NOT EXISTS UK_queries_hashed_name ON queries(hashed_name)""")

    conn.commit()
    conn.close()


# execute SELECT query
def select(query, placeholder=()):
    print('select')
    print(f'"query": "{query}"')
    assert len(query.split()) > 0
    assert query.split()[0] == 'SELECT'

    conn = mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        port=os.environ.get('DB_PORT'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        database=os.environ.get('DB_DATABASE'),
        charset='utf8mb4'
    )

    result = {}

    conn.start_transaction(readonly=True)

    cursor = None
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        if cursor:
            cursor.close()
        conn.close()

    return result


# register query
def register(name, query):
    print('register')
    print(f'"name": "{name}"')
    print(f'"query": "{query}"')
    assert name
    assert query

    data = (
        # ulid.new().int,
        ulid.new().str,
        name,
        query,
        # int(hashlib.sha256(name.encode()).hexdigest(), 16)
        hashlib.sha256(name.encode()).digest()
    )

    conn = sqlite3.connect(os.environ.get('INTERNAL_STORAGE'))
    
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO queries (id, name, query, hashed_name) VALUES (?, ?, ?, ?)', data)
        result = cursor.fetchall()
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        if cursor:
            cursor.close()
        conn.close()


# load query
def load(name):
    print('load')
    print(f'"name": "{name}"')
    assert name

    h = hashlib.sha256(name.encode()).digest()
    result = None

    conn = sqlite3.connect(os.environ.get('INTERNAL_STORAGE'))
    
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT query FROM queries WHERE hashed_name = ?', (h,))
        result = cursor.fetchone()[0]
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        if cursor:
            cursor.close()
        conn.close()

    return result


# list queries
def list():
    print('list')
    
    result = None

    conn = sqlite3.connect(os.environ.get('INTERNAL_STORAGE'))
    
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM queries')
        result = [x[0] for x in cursor.fetchall()]
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        if cursor:
            cursor.close()
        conn.close()

    return result


# search queries
def search(name, N=5):
    print('search')
    print(f'"name": "{name}"')
    assert name
    
    result = None
    t_select_all = None

    conn = sqlite3.connect(os.environ.get('INTERNAL_STORAGE'))
    
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT name FROM queries WHERE name LIKE ?', (f'%{name}%',))
        res1 = [x[0] for x in cursor.fetchall()]
        result = res1
        if len(result) < N:
            cursor.execute('SELECT name FROM queries')
            t_select_all = [x[0] for x in cursor.fetchall()]
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        if cursor:
            cursor.close()
        conn.close()

    
    if len(result) < N:
        ta = []
        for n in t_select_all:
            if n not in result:
                r = (alignment(name, n, False), n)
                ta.append(r)
        res2 = [y[1] for y in sorted(ta, key=lambda x: x[0][0], reverse=True)[0:N-len(result)]]
        result = result + res2

    if name in result:
        return [name]

    return result

