import pandas as pd
import sqlite3

def load_csv_data(file_path):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    return df

def save_to_sqlite(df, db_name="data/market_data.db", table_name="prices"):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

def load_from_sqlite(db_name="data/market_data.db", table_name="prices"):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df