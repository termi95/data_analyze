import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from db import execute_query

def sold_laptop_number_by_company_name():
    names, occurrences = zip(*execute_query("SELECT Company, COUNT(*) AS occurrences FROM laptops GROUP BY Company;"))
    fig = go.Figure(
    data=[go.Bar(y=occurrences,x=names)],
    layout_title_text="Zestawienie sprzedarz marka"
    )
    return fig.to_json()

def compare_weight_to_price():
    df = pd.DataFrame(execute_query("SELECT Weight, Price_euros FROM laptops"), columns=['Weight', 'Price_euros'])
    fig = px.scatter(df, x='Weight', y='Price_euros',trendline="ols",
                 labels={'Weight': 'Waga (kg)', 'Price_euros': 'Cena (EUR)'},
                 title='Zależność ceny do wagi laptopa')
    return fig.to_json()
