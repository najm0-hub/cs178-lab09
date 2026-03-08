# read_movies.py
# Reads items from the DynamoDB Movies table and allows searching by title.

import boto3
import boto3.dynamodb.conditions

# -------------------------------------------------------
# Configuration
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Books"


def get_table():
    """Connect to dynomodb."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_book(book):
    """Print a book in a readable format."""
    print("Title:", book.get("Title", "Unknown"))
    print("Author:", book.get("Author", "Unknown"))
    print("Genre:", book.get("Genre", "Unknown"))
    print("---------------------------")


def print_all_books():
    """Scan the table and print all books."""
    table = get_table()

    response = table.scan()
    items = response.get("Items", [])

    if not items:
        print("No books found in the table.")
        return

    print(f"Found {len(items)} book(s):\n")

    for book in items:
        print_book(book)


def main():
    print("===== Books Table =====\n")
    print_all_books()


if __name__ == "__main__":
    main()