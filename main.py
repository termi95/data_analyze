from flask import Flask, render_template
from db import recreate_db, get_data

app = Flask(__name__)
app.config['base_url'] = "http://127.0.0.1:5000"

@app.route("/")
def hello_world():
    recreate_db()
    return render_template("index.html", base_url=app.config['base_url'])

@app.route("/data")
def data():
    get_data()
    return render_template("data.html", base_url=app.config['base_url'])
