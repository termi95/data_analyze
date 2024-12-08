from flask import Flask, render_template, redirect
from db import recreate_db, is_database_empty
from services import *

app = Flask(__name__)
app.config['base_url'] = "http://127.0.0.1:5000"

@app.route("/")
def hello_world():
    return render_template("index.html", base_url=app.config['base_url'])

@app.route("/data")
def data():
    if is_database_empty():
        return render_template("empty.html", base_url=app.config['base_url'])
    else:
        total_laptops = get_total_laptops()
        most_common_cpu, cpu_count = get_most_common_cpu()
        average_ram = get_average_ram()
        lightest_laptop, lightest_weight = get_lightest_laptop()
        
        stats_data = {
            "total_laptops": total_laptops,
            "most_common_cpu": {"name": most_common_cpu, "count": cpu_count},
            "average_ram": average_ram,
            "lightest_laptop": {"name": lightest_laptop, "weight": lightest_weight}
        }

        return render_template(
            "data.html",
            base_url=app.config['base_url'],
            graphJSON=sold_laptop_number_by_company_name(),
            weightToPrice=compare_weight_to_price(),
            screenSizeDistribution=screen_size_distribution(),
            averagePriceByRam=average_price_by_ram(),
            storageTypeDistribution=storage_type_distribution(),
            resolutionVsPrice=resolution_vs_price(),
            stats=stats_data
        )
    
@app.route("/create-db", methods=["POST"])
def create_db():
    recreate_db()
    return redirect("/data")

if __name__ == "__main__":
    app.run(debug=True)