import sqlite3

from flask import g

from test_yourself import app


def add_question(question, ans1, ans2, correct):
    msg=""
    try:
        with sqlite3.connect("app.db") as con:
            cur=con.cursor()
            cur.execute("""INSERT INTO drivers_test
                        (question, ans1, ans2, correct) VALUES (?,?,?,?)""",
                        (question,ans1,ans2,correct))
            con.commit()
            msg="Recors successfully added"
    except:
        con.rollback()
        msg="ERRRR"
    finally:
        con.close()
        return msg
def get_db():
    db=getattr(g,"_database",None)
    if db is None:
        db=g._database=sqlite3.connect("app.db")
        cursor=db.cursor()
        cursor.execute("select * from drivers_test")
        return cursor.fetchall()
@app.teardown_appcontext
def close_connection(ex):
    db=getattr(g,"_database",None)
    if db is not None:
        db.close()
