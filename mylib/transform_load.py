"""
Transforms and Loads data into the local SQLite3 database
"""

import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/candy-data.csv"):
    """ "Transforms and Loads data into the local databricks database"""

    df = pd.read_csv(dataset, delimiter=",", skiprows=1)
    load_dotenv()
    server_h = os.getenv("SQL_SERVER_HOST")
    access_token = os.getenv("DATABRICKS_API_KEY")
    http_path = os.getenv("SQL_HTTP")
    with sql.connect(
        server_hostname=server_h, http_path=http_path, access_token=access_token
    ) as connection:
        c = connection.cursor()
        c.execute("SHOW TABLES FROM default LIKE 'keh119*'")
        result = c.fetchall()
        if result:  # see if its already there so we dont duplicate in DataBricks
            print("keh119_Candy already exists, skipping data load")
            return "success"
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS keh119_Candy(
                competitorname string,
                chocolate int,
                fruity int,
                caramel int,
                peanutyalmondy int,
                nougat int,
                crispedricewafer int,
                hard int,
                bar int,
                pluribus int,
                sugarpercent float,
                pricepercent float,
                winpercent float
                )
            """
            )
        # Insert rows from the DataFrame into the database
        for _, row in df.iterrows():
            # Use placeholders and convert the DataFrame row to a tuple
            c.execute(
                """
                INSERT INTO keh119_Candy (
                    competitorname, chocolate, fruity, caramel, 
                    peanutyalmondy, nougat, 
                    crispedricewafer, hard, bar, pluribus, 
                    sugarpercent, pricepercent, winpercent
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                tuple(row),
            )

        # Commit the transaction and close the cursor
        connection.commit()
        c.close()

    # uses this as a test to make sure the assert statement runs
    return "success"


if __name__ == "__main__":
    load()
