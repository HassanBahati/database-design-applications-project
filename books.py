import csv
from cs50 import SQL

# open database 
open("books.db", "w").close()

db=SQL("sqlite:///books.db")

# create table authors
db.execute("CREATE TABLE authors (id INTEGER, name TEXT, PRIMARY KEY(id))")

# create table books
db.execute("CREATE TABLE books (id INTEGER, title TEXT, PRIMARY KEY(id))")

# create table sales
db.execute("CREATE TABLE sales (id INTEGER, quantity INTEGER, PRIMARY KEY(id))")

#create table collection
db.execute("CREATE TABLE collection (book_id INTEGER, collection TEXT, FOREIGN KEY(book_id) REFERENCES books(id))" )

# connecting table stars
db.execute("CREATE TABLE stars (author_id INTEGER, book_id INTEGER, FOREIGN KEY(author_id) REFERENCES authors(id), FOREIGN KEY(book_id) REFERENCES books(id))")

# connecting table receipts
db.execute("CREATE TABLE receipts (sales_id INTEGER, book_id INTEGER, FOREIGN KEY(sales_id) REFERENCES sales(id), FOREIGN KEY(book_id) REFERENCES books(id))")

# connecting table rating
db.execute("CREATE TABLE rating (book_id INTEGER, rating INTEGER, FOREIGN KEY(book_id) REFERENCES books(id))")

with open("books.csv", "r") as file:
    #store in file called reader
    reader = csv.DictReader(file)

    for row in reader:
        # get title and store in a variable title 
        title = row["Title"].strip().capitalize()
        name = row["Author"].strip().capitalize()
        rating = row["Rating"]
        quantity = row["Sales"]


        #insert data into athours table 
        author_id=db.execute("INSERT INTO authors (name) VALUES(?)", name)

        #insert data into books table 
        book_id=db.execute("INSERT INTO books (title) VALUES(?)", title)
        
        #insert data int stars table 
        db.execute("INSERT INTO stars (author_id,book_id) VALUES(?,?)", author_id,book_id)

        #insert data into sales table 
        sales_id=db.execute("INSERT INTO sales (quantity) VALUES(?)", quantity)

        #insert data int receipts table 
        db.execute("INSERT INTO receipts (sales_id,book_id) VALUES(?,?)", sales_id,book_id)

        #insert data int rating table 
        db.execute("INSERT INTO rating (book_id,rating) VALUES(?,?)", book_id,rating)

        for collection in row["Collection"].split(","):
            
            #insert data into collection table
            db.execute("INSERT INTO collection (book_id, collection) VALUES(?,?)", book_id, collection)