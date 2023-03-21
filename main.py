import sqlite3
connection=sqlite3.connect("test_yourself/app.db")
print('da')
connection.execute("CREATE TABLE test_yourself (question TEXT, ans1 TEXT, ans2 TEXT, correct TEXT)")
print('ok')
connection.close()