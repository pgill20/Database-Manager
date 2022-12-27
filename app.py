
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/coaches')
def coaches():
    return render_template("coaches.html")

@app.route('/players')
def players():
    return render_template("players.html")

@app.route('/teams')
def teams():
    return render_template("teams.html")

@app.route('/stadiums')
def stadiums():
    return render_template("stadiums.html")

@app.route('/trainers')
def trainers():
    return render_template("trainers.html")

@app.route('/players_trainers')
def players_trainers():
    return render_template("players_trainers.html")
