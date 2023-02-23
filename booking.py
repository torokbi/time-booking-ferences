from flask import Flask, redirect, url_for, render_template
from data import events

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("student.html",events=events)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/forgot-pw")
def forgot_pw():
    return render_template("forgot.html")

if __name__ == '__main__':
    app.run(debug=True)