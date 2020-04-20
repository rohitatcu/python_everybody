

import sqlite3


conn = sqlite3.connect('Ages')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')

cur.execute('''
CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)
''')


cur.execute('''
INSERT INTO Ages (name, age) VALUES ('Brieghanna', 37);
''')


cur.execute('''
SELECT hex(name || age) AS X FROM Ages ORDER BY X
''')
