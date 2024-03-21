from files import BOOKS_CSV_FILE_PATH, USERS_JSON_FILE_PATH, RESULT_JSON_FILE_PATH
from csv import DictReader
import json
import itertools


with (
    open(BOOKS_CSV_FILE_PATH) as books_file,
    open(USERS_JSON_FILE_PATH) as users_file,
    open(RESULT_JSON_FILE_PATH, "w") as result_file,
):
    books = DictReader(books_file)

    users = [
        {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": [],
        }
        for user in json.load(users_file)
    ]

    for book, user in zip(books, itertools.cycle(users)):
        user["books"].append(
            {
                "title": book["Title"],
                "author": book["Author"],
                "pages": book["Pages"],
                "genre": book["Genre"],
            }
        )
    json.dump(users, result_file, indent=4)
