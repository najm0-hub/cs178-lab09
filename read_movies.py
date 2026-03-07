# read_movies.py
# Reads items from the DynamoDB Movies table and allows searching by title.

import boto3

# -------------------------------------------------------
# Configuration
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Movies"


def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_movie(movie):
    """Print movie details."""
    print("Title:", movie.get("Title"))
    print("Year:", movie.get("Year"))
    print("Genre:", movie.get("Genre", "N/A"))
    print("---------------------")


def print_all_movies():
    """Print all movies in the table."""
    table = get_table()

    response = table.scan()
    items = response.get("Items", [])

    if not items:
        print("No movies found.")
        return

    print(f"Found {len(items)} movie(s):\n")

    for movie in items:
        print_movie(movie)


def get_movie_by_title():
    """Prompt user for a title and search the table."""
    table = get_table()

    title = input("Enter movie title: ")

    response = table.scan(
        FilterExpression="Title = :t",
        ExpressionAttributeValues={
            ":t": title
        }
    )

    items = response.get("Items", [])

    if items:
        print("\nMovie found:\n")
        for movie in items:
            print_movie(movie)
    else:
        print("\nMovie not found.")


def main():
    print("===== DynamoDB Movies =====\n")

    print_all_movies()

    print("\nSearch for a movie")
    get_movie_by_title()


if __name__ == "__main__":
    main()