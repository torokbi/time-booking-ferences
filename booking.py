from flask import Flask, redirect, url_for, render_template
from data import events

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("student.html",events=events)


@app.route("/events")
def event_manage ():
    datas = events.copy()
    for first in range(0,len(datas)):
        for second in range(first+1,len(datas)):
            if datas[first]["colum"] > datas[second]["colum"]:
                    datas[first],datas[second] = datas[second],datas[first]
    for first in range(0,len(datas)):
        for second in range(first+1,len(datas)):
            if datas[first]["name"] > datas[second]["name"] and datas[first]["colum"] == datas[second]["colum"]:
                    datas[first],datas[second] = datas[second],datas[first]

    return render_template("events.html",events=datas)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/forgot-pw")
def forgot_pw():
    return render_template("forgot.html")

if __name__ == '__main__':
    app.run(debug=True)