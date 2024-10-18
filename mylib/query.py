"""Query the database from a db connection to Databricks"""

import os
from databricks import sql
from dotenv import load_dotenv

complex_query = """
WITH avg_winpercent AS ( 
SELECT  
chocolate, 
AVG(winpercent) AS choc_nonchoc_win_perc 
FROM  default.keh119_candy 
GROUP BY  chocolate 
) 

SELECT  
keh.competitorname, 
keh.winpercent, 
avg_winpercent.choc_nonchoc_win_perc 
FROM default.keh119_candy as keh 
JOIN avg_winpercent 
ON keh.chocolate = avg_winpercent.chocolate 
ORDER BY keh.winpercent DESC;  
"""


def my_query():
    """runs a query"""
    load_dotenv()
    server_h = os.getenv("SQL_SERVER_HOST")
    access_token = os.getenv("DATABRICKS_API_KEY")
    http_path = os.getenv("SQL_HTTP")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        with connection.cursor() as cursor:

            cursor.execute(complex_query)
            result = cursor.fetchall()

            for row in result:
                print(row)

            cursor.close()
            connection.close()
    return "query successful"


if __name__ == "__main__":
    my_query()
