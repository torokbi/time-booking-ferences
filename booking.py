from flask import Flask, redirect, url_for, render_template, request
from data import events
from forms import Neweventform

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fshghb162167t8jvbnodbndnb'

@app.route("/")
def home():
    return render_template("student.html",events=events)


@app.route("/events")
def event_manager ():
    datas = events.copy()
    form = Neweventform()
    for first in range(0,len(datas)):
        for second in range(first+1,len(datas)):
            if datas[first]["colum"] > datas[second]["colum"]:
                    datas[first],datas[second] = datas[second],datas[first]
    for first in range(0,len(datas)):
        for second in range(first+1,len(datas)):
            if datas[first]["name"] > datas[second]["name"] and datas[first]["colum"] == datas[second]["colum"]:
                    datas[first],datas[second] = datas[second],datas[first]

    return render_template("events.html",events=datas, form=form)


@app.route("/events/new", methods=["GET","POST"])
def event_new():
     form = Neweventform()
     if request.method == "POST":
        for index in form.column.data:
            if index[0] == "A":
                events.append({'name': form.title.data, 'tutor': form.tutor.data, 'colum':1, 'description': form.description.data, 'location': form.location.data, 'seat':form.seat.data})
            elif index[0] == "B":
                events.append({'name': form.title.data, 'tutor': form.tutor.data, 'colum':2, 'description': form.description.data, 'location': form.location.data, 'seat':form.seat.data})
            elif index[0] == "C":
                events.append({'name': form.title.data, 'tutor': form.tutor.data, 'colum':3, 'description': form.description.data, 'location': form.location.data, 'seat':form.seat.data})
     return redirect(url_for("event_manager"))


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/forgot-pw")
def forgot_pw():
    return render_template("forgot.html")

if __name__ == '__main__':
    app.run(debug=True)