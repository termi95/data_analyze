import os.path
import sqlite3 as lite
from pathlib import Path
from .microorm import execute_non_query, executemany_non_query, execute_query
import pandas as pd

DB_FILE_NAME = 'laptop_prices.db'
CRATE_TABLE_FILE_NAME = 'crate_table_laptops.sql'
INSERT_LAPTOPS_FILE_NAME = 'insert_laptop.sql'
SELECT_LAPTOPS_FILE_NAME = 'select_laptop.sql'
LAPTOPS_FILE_NAME = 'laptop_prices.csv'

def create_db()->None:
    if not os.path.isfile(DB_FILE_NAME):
        create_table()
        insert_data()
    else:
        print("Database already exist")

def recreate_db()->None:
    if os.path.isfile(DB_FILE_NAME):
        os.remove(DB_FILE_NAME)
    create_db()    

def create_table()->None:
    execute_non_query(get_sql_by_name(CRATE_TABLE_FILE_NAME))

def insert_data()->None:
    executemany_non_query(get_sql_by_name(INSERT_LAPTOPS_FILE_NAME),load_csv_to_params())

def get_connection()->lite.Connection:
    return lite.connect(DB_FILE_NAME)

def get_sql_by_name(name:str) -> str:
    paht = Path.joinpath(Path(__file__).parent, 'sql', name)
    with open(paht, "r") as file:
        content = file.read()
    return content

def load_csv_to_params()->list:
    df = pd.read_csv(LAPTOPS_FILE_NAME)
    params_list = []    
    
    for _, row in df.iterrows():
        row_dict = row.to_dict()        
        params_list.append(row_dict)    
    
    return params_list

def get_data():    
    data = execute_query(get_sql_by_name(SELECT_LAPTOPS_FILE_NAME))
    if data is not None:
        for item in data:
            print(item)
