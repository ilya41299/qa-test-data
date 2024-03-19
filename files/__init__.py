from pathlib import Path

ROOT_DIR = Path(__file__).parent

BOOKS_CSV_FILE_PATH = Path.joinpath(ROOT_DIR, "books.csv")
USERS_JSON_FILE_PATH = Path.joinpath(ROOT_DIR, "users.json")
RESULT_JSON_FILE_PATH = Path.joinpath(ROOT_DIR, "result.json")
