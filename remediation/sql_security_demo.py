import sqlite3
import logging
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parent / "security.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_database():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE Products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT
        )
    """)

    cursor.executemany(
        "INSERT INTO Products (name, description) VALUES (?, ?)",
        [
            ("Apple Juice", "Fresh apple juice"),
            ("Ben's Juice", "Fresh fruit juice")
        ]
    )

    connection.commit()
    return connection


def secure_search(connection, user_input):
    try:
        cursor = connection.cursor()
        search_pattern = "%" + user_input + "%"

        cursor.execute(
            "SELECT * FROM Products WHERE name LIKE ?",
            (search_pattern,)
        )

        return cursor.fetchall()

    except sqlite3.Error as error:
        logging.error("Database search failed: %s", error)
        print("Unable to complete the search.")
        return None


if __name__ == "__main__":
    connection = create_database()

    print("Database created successfully")

    print("Test 1:", secure_search(connection, "Apple"))
    print("Test 2:", secure_search(connection, "Ben's Juice"))
    print("Test 3:", secure_search(connection, "80's"))
    print("Test 4:", secure_search(connection, "xyz123abc"))

    print("\nTesting database failure:")
    connection.close()

    print("Result:", secure_search(connection, "Apple"))