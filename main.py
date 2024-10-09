"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create, read, update, delete

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# Query
print("Querying data...")
print(
    "------------------------------------------------------------------------------------------------------------------------------------------------"
)
print("Create a row for fake candy 'Data Engineering'")
create()
read()
print(
    "------------------------------------------------------------------------------------------------------------------------------------------------"
)
print("Update competitorname in DB to be 'LOSER' when winpercent <50%")
update()
read()
print(
    "------------------------------------------------------------------------------------------------------------------------------------------------"
)
print("Delete LOSERS")
delete()
read()
