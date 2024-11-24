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

def screen_size_distribution():
    df = pd.DataFrame(execute_query("SELECT Inches FROM laptops"), columns=['Inches'])
    fig = px.histogram(df, x="Inches", nbins=15,
                       labels={'Inches': 'Rozmiar ekranu (cale)'},
                       title="Rozkład wielkości ekranów laptopów")
    return fig.to_json()

def average_price_by_ram():
    df = pd.DataFrame(execute_query("SELECT Ram, AVG(Price_euros) AS AvgPrice FROM laptops GROUP BY Ram"), columns=['Ram', 'AvgPrice'])
    fig = px.bar(df, x="Ram", y="AvgPrice",
                 labels={'Ram': 'Pamięć RAM (GB)', 'AvgPrice': 'Średnia cena (EUR)'},
                 title="Średnia cena laptopa w zależności od pamięci RAM")
    return fig.to_json()

def storage_type_distribution():
    df = pd.DataFrame(execute_query("SELECT PrimaryStorageType, COUNT(*) AS Count FROM laptops GROUP BY PrimaryStorageType"), columns=['PrimaryStorageType', 'Count'])
    fig = px.pie(df, values="Count", names="PrimaryStorageType",
                 title="Udział różnych typów pamięci w laptopach")
    return fig.to_json()

def resolution_vs_price():
    df = pd.DataFrame(execute_query("SELECT ScreenW, ScreenH, Price_euros FROM laptops"), columns=['ScreenW', 'ScreenH', 'Price_euros'])
    df['Resolution'] = df['ScreenW'] * df['ScreenH']
    fig = px.scatter(df, x='Resolution', y='Price_euros', trendline="ols",
                     labels={'Resolution': 'Rozdzielczość ekranu (px)', 'Price_euros': 'Cena (EUR)'},
                     title='Zależność ceny od rozdzielczości ekranu')
    return fig.to_json()

def get_total_laptops():
    query = "SELECT COUNT(DISTINCT Product) FROM laptops"
    result = execute_query(query)
    return result[0][0] if result else 0

def get_most_common_cpu():
    query = """
    SELECT CPU_model, COUNT(*) AS count
    FROM laptops
    GROUP BY CPU_model
    ORDER BY count DESC
    LIMIT 1
    """
    result = execute_query(query)
    return result[0] if result else ("Brak danych", 0)

def get_average_ram():
    query = "SELECT AVG(RAM) FROM laptops"
    result = execute_query(query)
    return round(result[0][0]) if result else 0

def get_lightest_laptop():
    query = """
    SELECT Product, Weight
    FROM laptops
    ORDER BY Weight ASC
    LIMIT 1
    """
    result = execute_query(query)
    return result[0] if result else ("Brak danych", 0)