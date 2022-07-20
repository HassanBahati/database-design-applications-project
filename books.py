import csv
from cs50 import SQL

# open database 
open("books.db", "w").close()

db=SQL("sqlite:///books.db")

# create table authors
db.execute("CREATE TABLE authors (id INTEGER, name TEXT, nationality TEXT, PRIMARY KEY(id))")

#create table books
db.execute("CREATE TABLE books (id INTEGER, title TEXT, publisher TEXT, edition INTEGER, PRIMARY KEY(id))" )

# connecting table stars
db.execute("CREATE TABLE stars (book_id INTEGER, author_id INTEGER, FOREIGN KEY(book_id) REFERENCES books(id), FOREIGN KEY(author_id) REFERENCES authors(id))")

#create table collections
db.execute("CREATE TABLE collections (book_id INTEGER, collection TEXT, FOREIGN KEY(id) REFERENCES books(id))" )

#create table rating
db.execute("CREATE TABLE rating (book_id INTEGER, rating TINTEGER, FOREIGN KEY(id) REFERENCES books(id))" )

#create table sales
db.execute("CREATE TABLE sales (id INTEGER, quantity TINTEGER, PRIMARY KEY(id))" )

# connecting table receipts
db.execute("CREATE TABLE receipts (book_id INTEGER, sales_id INTEGER, FOREIGN KEY(book_id) REFERENCES books(id), FOREIGN KEY(sales_id) REFERENCES sales(id))")



with open("books.csv", "r") as file:
    #store in file called reader
    reader = csv.DictReader(file)

    for row in reader:
        # get title and store in a variable title 
        title = row["Film"].strip().capitalize()

        #insert data into movies table 
        movies_id=db.execute("INSERT INTO movies (title) VALUES(?)", title)

        for genre in row["Genre"].split(","):
            
            #insert data into genre table
            genre_id=db.execute("INSERT INTO genre (id, genre) VALUES(?,?)", movies_id, genre)

            db.execute("INSERT INTO connect (movie_id,genre_id) VALUES(?,?)", movies_id,genre_id)

