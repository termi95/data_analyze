from flask import Flask, render_template
from db import recreate_db, get_data

app = Flask(__name__)

@app.route("/")
def hello_world():
    recreate_db()
    return render_template("index.html")

@app.route("/data")
def data():
    get_data()
    return render_template("data.html")
