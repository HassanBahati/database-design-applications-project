import csv
from cs50 import SQL

# open database 
open("books.db", "w").close()

db=SQL("sqlite:///books.db")

# create table movies
db.execute("CREATE TABLE movies (id INTEGER, title TEXT, PRIMARY KEY(id))")

# connecting table 
db.execute("CREATE TABLE connect (movie_id INTEGER, genre_id INTEGER, FOREIGN KEY(movie_id) REFERENCES movies(id), FOREIGN KEY(genre_id) REFERENCES genre(id))")

#create table genre
db.execute("CREATE TABLE genre (id INTEGER, genre TEXT, FOREIGN KEY(id) REFERENCES movies(id))" )


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

