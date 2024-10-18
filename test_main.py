"""
Test goes here
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import my_query


def test_extract():
    assert extract() == "data/candy-data.csv"


def test_load():
    assert load() == "success"


def test_my_query():
    assert my_query() == "query successful"


if __name__ == "__main__":
    test_extract()
    test_load()
    test_my_query()
