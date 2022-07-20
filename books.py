import csv
from cs50 import SQL

# open database 
open("gross_movies_db.db", "w").close()

db=SQL("sqlite:///gross_movies_db.db")

# create table movies
db.execute("CREATE TABLE movies (id INTEGER, title TEXT, PRIMARY KEY(id))")

#create table genre
db.execute("CREATE TABLE genre (movie_id INTEGER, genre TEXT, FOREIGN KEY(movie_id) REFERENCES movies(id))" )

with open("gross movies.csv", "r") as file:
    #store in file called reader
    reader = csv.DictReader(file)

    for row in reader:
        # get title and store in a variable title 
        title = row["Film"].strip().capitalize()

        #insert data into movies table 
        id=db.execute("INSERT INTO movies (title) VALUES(?)", title)

        for genre in row["Genre"].split(","):
            
            #insert data into genre table
            db.execute("INSERT INTO genre (movie_id, genre) VALUES(?,?)", id, genre)