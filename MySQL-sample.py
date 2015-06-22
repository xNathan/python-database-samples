#! /usr/bin/python

import MySQLdb as mdb
import sys


USERNAME = 'root'
PASSWORD = '123456'
SERVER_IP = 'localhost'
PORT = '3306'
DATABASE_NAME = 'test_python'
TABLE_NAME = 'test'

try:
    conn = mdb.connect(SERVER_IP, USERNAME, PASSWORD, DATABASE_NAME)
except Exception, e:
    print e
    sys.exit(1)

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS test')
cur.execute('CREATE TABLE test(id INT PRIMARY KEY AUTO_INCREMENT, \
            value VARCHAR(25))')

# Add
cur.execute('INSERT INTO test(value) VALUES(%s)', ('ab',))

#'''This a sample of executemany
cur.executemany('INSERT INTO test(value) VALUES(%s)', (
    ('d',),
    ('e',),
    ('f',),
))
#'''

# Delete
cur.execute('DELETE FROM test WHERE id=%s', (2,))

# Update
cur.execute('UPDATE test SET value=%s WHERE id=%s', ('abck', 3))
cur.execute('SELECT * FROM test')
print cur.fetchall()
# Search

conn.commit()
conn.close()
