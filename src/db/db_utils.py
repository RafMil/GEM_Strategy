import psycopg2
from psycopg2.extras import execute_values
import os

def get_connection():
    """Create a database connection using environment variables."""
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        port=os.getenv("DB_PORT", 5432)
    )

def save_dataframe(df, table_name: str):
    """Save a pandas DataFrame into PostgreSQL."""
    conn = get_connection()
    cur = conn.cursor()
    records = df.reset_index().to_dict("records")

    # INSERT — wersja minimalna
    execute_values(
        cur,
        f"INSERT INTO {table_name} ({','.join(records[0].keys())}) VALUES %s",
        [tuple(r.values()) for r in records]
    )
    conn.commit()
    cur.close()
    conn.close()
