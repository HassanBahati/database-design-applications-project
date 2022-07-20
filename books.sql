CREATE DATABASE BH ;


CREATE TABLE authors(
    id INTEGER PRIMARY KEY AUTO INCREMENT,
    name TEXT,
    nationality TEXT
    );


CREATE TABLE books(
    id INTEGER PRIMARY KEY AUTO INCREMENT,
    title TEXT,
    publisher TEXT,
    edition INTEGER,
    );


CREATE TABLE stars(
    book_id INTEGER,
    author_id INTEGER,
    FOREIGN KEY(book_id) REFERENCES books(id), 
    FOREIGN KEY(author_id) REFERENCES authors(id)
    );

CREATE TABLE collections(
    book_id INTEGER ,
    collection TEXT,
    FOREIGN KEY(book_id) REFERENCES books(id),
    );

CREATE TABLE rating(
    book_id INTEGER ,
    rating INTEGER,
    FOREIGN KEY(book_id) REFERENCES books(id),
    );

CREATE TABLE sales(
    id INTEGER PRIMARY KEY AUTO INCREMENT,
    quantity INTEGER,
    );

CREATE TABLE receipts(
    book_id INTEGER ,
    sales_id INTEGER,
    FOREIGN KEY(book_id) REFERENCES books(id),
    FOREIGN KEY(sales_id) REFERENCES sales(id)
    );