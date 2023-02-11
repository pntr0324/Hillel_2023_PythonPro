import sqlite3


def select_query_db(query1):
    conn = sqlite3.connect('vacancy.db')
    c = conn.cursor()
    c.execute(query1)
    result = c.fetchall()
    conn.close()
    return result


def insert_db(table_name, data):
    columns = ', '.join(data.keys())
    placeholders = ':' + ', :'.join(data.keys())
    query = 'INSERT INTO %s (%s) VALUES (%s)' % (table_name, columns, placeholders)
    conn = sqlite3.connect('vacancy.db')
    c = conn.cursor()
    c.execute(query, data)
    conn.commit()
    conn.close()
