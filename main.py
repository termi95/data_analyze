from flask import Flask
from db import recreate_db, get_data

app = Flask(__name__)

@app.route("/")
def hello_world():
    recreate_db()
    return "<p>Hello, World!</p>"

@app.route("/data")
def data():
    get_data()
    return "<p>data!</p>"
