import sqlite3 as lite

DB_FILE_NAME = 'laptop_prices.db'

def get_connection()->lite.Connection:
    return lite.connect(DB_FILE_NAME)

def execute_non_query(sql:str, parameters=None)->None:
    conn = get_connection()
    cursor = conn.cursor()
        
    try:
        if parameters is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, parameters)
        conn.commit()
    except lite.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()
        
def executemany_non_query(sql:str, parameters=None)->None:
    conn = get_connection()    
    conn.isolation_level = None 
    cursor = conn.cursor()
    
    try:
        cursor.executemany(sql, parameters)
        conn.commit()
    except lite.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def execute_query(sql:str, parameters=None) -> list[any] | None:
    conn = get_connection()
    cursor = conn.cursor()
    data = None
        
    try:
        if parameters is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, parameters)

        data = cursor.fetchall()
    except lite.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()
        
    return data