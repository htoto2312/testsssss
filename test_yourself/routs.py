
from flask import render_template,request

from test_yourself import app, db_controls
from test_yourself.db_controls import add_question


@app.route('/home')
@app.route("/")
def home():
    return render_template("base.html")
@app.route('/add_test',methods=["GET","POST"])
def add_test():
    if request.method=="POST":
        question=request.form["question"]
        ans1=request.form["ans1"]
        ans2=request.form["ans2"]
        correct=request.form["correct"]
        msg=add_question(question,ans1,ans2,correct)
        return msg
    return render_template("add_test.html")
@app.route("/drivers_test",methods=["GET","POST"])
def drivers_test():
    all_data=db_controls.get_db()
    return render_template("drivers_test.html",all_data=all_data)
