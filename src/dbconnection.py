import pandas as pd
from sqlalchemy import create_engine


def create_database_connection():
    
    db_params = {
        'host': 'localhost',
        'port': '5432',
        'user': 'postgres',
        'password': 'lawofatt7',
        'database': 'tele',
    }

    # Create a SQLAlchemy engine
    engine = create_engine(f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}")

    return engine

def read_data_into_dataframe(engine, table_name):
    # SQL query to fetch data from a table 
    query = f"SELECT * FROM xdr_data;"

    # read the SQL query result into a DataFrame
    df = pd.read_sql_query(query, engine)

    return df
