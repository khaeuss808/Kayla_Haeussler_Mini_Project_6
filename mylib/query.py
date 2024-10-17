"""Query the database from a db connection to Databricks"""

import os
from databricks import sql
from dotenv import load_dotenv


def my_query(query):
    """runs a query"""
    load_dotenv()
    server_h = os.getenv("sql_server_host")
    access_token = os.getenv("databricks_api_key")
    http_path = os.getenv("sql_http")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c=connection.cursor()
        c.execute(
            WITH 
        )
        result = c.fetchall()
    
    c.close

if __name__ == "__main__":
 
