"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import my_query

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

print("Querying data...")
my_query()
