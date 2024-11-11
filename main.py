from flask import Flask, render_template
from db import recreate_db, get_data
from services import sold_laptop_number_by_company_name, compare_weight_to_price

app = Flask(__name__)
app.config['base_url'] = "http://127.0.0.1:5000"

@app.route("/")
def hello_world():
    # recreate_db()
    return render_template("index.html", base_url=app.config['base_url'])

@app.route("/data")
def data():
    # get_data()
    return render_template("data.html", base_url=app.config['base_url'], graphJSON=sold_laptop_number_by_company_name(), weightToPrice=compare_weight_to_price())

if __name__ == "__main__":
    app.run(debug=True)