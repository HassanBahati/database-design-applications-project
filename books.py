import csv
from cs50 import SQL

# open database
open("books.db", "w").close()

db = SQL("sqlite:///books.db")

# create table authors
db.execute(
    "CREATE TABLE authors (id INTEGER, name TEXT, nationality TEXT, PRIMARY KEY(id))")

# create table books
db.execute("CREATE TABLE books (id INTEGER, title TEXT, publisher TEXT, edition INTEGER, PRIMARY KEY(id))")

# connecting table stars
db.execute("CREATE TABLE stars (book_id INTEGER, author_id INTEGER, FOREIGN KEY(book_id) REFERENCES books(id), FOREIGN KEY(author_id) REFERENCES authors(id))")

# create table collections
db.execute("CREATE TABLE collections (book_id INTEGER, collection TEXT, FOREIGN KEY(id) REFERENCES books(id))")

# create table rating
db.execute(
    "CREATE TABLE rating (book_id INTEGER, rating INTEGER, FOREIGN KEY(id) REFERENCES books(id))")

# create table sales
db.execute("CREATE TABLE sales (id INTEGER, quantity INTEGER, PRIMARY KEY(id))")

# connecting table receipts
db.execute("CREATE TABLE receipts (book_id INTEGER, sales_id INTEGER, FOREIGN KEY(book_id) REFERENCES books(id), FOREIGN KEY(sales_id) REFERENCES sales(id))")


with open("books.csv", "r") as file:
    # store in file called reader
    reader = csv.DictReader(file)

    for row in reader:
        # get book title,publisher,edition and store in variables
        title = row["Title"].strip().capitalize()
        publisher = row["Publisher"].strip().capitalize()
        edition = row["Edition"].strip()

        # author table
        name = row["Author"].strip().capitalize()
        nationality = row["Nationality"].strip().capitalize()

        # rating
        rating = row["Rating"].strip()

        # sales quantity
        quantity = row["Sales"].strip()

        # insert data into books table
        book_id = db.execute(
            "INSERT INTO books (title,publisher,edition) VALUES(?,?,?)", title, publisher, edition)

        # insert data into authors table
        author_id = db.execute(
            "INSERT INTO authors (name,nationality) VALUES(?,?)", name, nationality)

        # insert data into stars table
        db.execute(
            "INSERT INTO stars (book_id,author_id) VALUES(?,?)", book_id, author_id)

        # insert data into rating table
        db.execute(
            "INSERT INTO rating (book_id,rating) VALUES(?,?)", book_id, rating)

        # insert data into sales quantity table
        sales_id = db.execute(
            "INSERT INTO sales (book_id,quantity) VALUES(?,?)", book_id, quantity)

        # insert data into rating table
        db.execute(
            "INSERT INTO receipts (book_id,sales_id) VALUES(?,?)", book_id, sales_id)

        for collection in row["Collection"].strip().capitalize():

            # insert data into collections table
            db.execute(
                "INSERT INTO genre (book_id, collection) VALUES(?,?)", book_id, collection)
