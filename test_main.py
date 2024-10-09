"""
Test goes here

"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import create, read, update, delete


def test_extract():
    assert extract() == "data/candy-data.csv"


def test_load():
    assert load() == "Candy_DB.db"


def test_create():
    assert create() == "Sucessfully created!"


def test_read():
    assert read() == "Successfully read!"


def test_update():
    assert update() == "Successfully updated!"


def test_delete():
    assert delete() == "Sucessfully deleted!"


if __name__ == "__main__":
    test_extract()
    test_load()
    test_create()
    test_read()
    test_update()
    test_delete()
