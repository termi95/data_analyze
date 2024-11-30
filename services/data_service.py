import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from db import execute_query

import plotly.graph_objects as go

def sold_laptop_number_by_company_name():
    names, occurrences = zip(*execute_query("SELECT Company, COUNT(*) AS occurrences FROM laptops GROUP BY Company;"))

    fig = go.Figure(
        data=[
            go.Scatter(
                x=names,
                y=occurrences,
                mode='markers+text',
                marker=dict(
                    size=[x * 10 for x in occurrences],
                    sizemode='area',
                    sizeref=max(occurrences) / 100,
                    sizemin=15,
                    color=occurrences,
                    colorscale='Viridis',
                    showscale=True
                ),
                text=occurrences,
                textposition="top center"
            )
        ]
    )

    fig.update_layout(
        title="Sprzedaż laptopów według marki",
        xaxis=dict(title="Marka", tickangle=45),
        yaxis=dict(title="Liczba sprzedanych laptopów", rangemode="tozero"),
        height=600
    )

    return fig.to_json()

def compare_weight_to_price():
    df = pd.DataFrame(execute_query("SELECT Weight, Price_euros FROM laptops"), columns=['Weight', 'Price_euros'])

    fig = px.scatter(
        df,
        x='Weight',
        y='Price_euros',
        trendline="ols",
        labels={
            'Weight': 'Waga (kg)',
            'Price_euros': 'Cena (EUR)'
        },
        title='Zależność ceny do wagi laptopa'
    )
    fig.update_traces(
        marker=dict(size=10, color='rgba(30,144,255,0.7)', line=dict(width=1, color='DarkSlateGrey')),
        selector=dict(mode='markers')
    )
    fig.update_traces(
        line=dict(color='red', width=3),
        selector=dict(mode='lines')
    )
    fig.update_layout(
        xaxis=dict(title="Waga (kg)", rangemode="tozero", gridcolor='LightGrey'),
        yaxis=dict(title="Cena (EUR)", rangemode="tozero", gridcolor='LightGrey'),
        font=dict(size=14),
        plot_bgcolor='white',
        height=600
    )

    return fig.to_json()

def screen_size_distribution():
    df = pd.DataFrame(execute_query("SELECT Inches FROM laptops"), columns=['Inches'])

    fig = px.histogram(
        df,
        x="Inches",
        nbins=15,
        labels={'Inches': 'Rozmiar ekranu (cale)'},
        title="Rozkład wielkości ekranów laptopów",
        template="simple_white"
    )

    fig.update_layout(
        xaxis=dict(title="Rozmiar ekranu (cale)", gridcolor='LightGrey'),
        yaxis=dict(title="Liczba laptopów", gridcolor='LightGrey'),
        font=dict(size=14),
        height=600,
    )

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
    df['Resolution_label'] = df['ScreenW'].astype(str) + ' x ' + df['ScreenH'].astype(str)
    
    fig = px.scatter(df, 
                     x='Resolution', 
                     y='Price_euros', 
                     trendline="ols",
                     color='Resolution',
                     size_max=10,
                     hover_data=['Resolution_label'],
                     labels={'Resolution': 'Rozdzielczość ekranu (px)', 'Price_euros': 'Cena (EUR)', 'Resolution_label': 'Rozdzielczość ekranu'},
                     title='Zależność ceny od rozdzielczości ekranu')
    
    fig.update_traces(marker=dict(size=8, opacity=0.6, line=dict(width=1, color='DarkSlateGrey')))
    
    fig.update_layout(
        plot_bgcolor='white',
        title_font=dict(size=20),
        xaxis=dict(tickmode='linear', tick0=0, dtick=10000000),
        yaxis=dict(tickformat='.2f'),
        coloraxis_colorbar=dict(title="Rozdzielczość ekranu (px)")
    )
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