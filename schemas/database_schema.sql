CREATE TABLE Product (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    quantity_in_stock INTEGER NOT NULL
);

CREATE TABLE Category (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    parent_category_id INTEGER,
    FOREIGN KEY (parent_category_id) REFERENCES Category(id)
);

CREATE TABLE User (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT DEFAULT 'user',
    email TEXT
);

CREATE TABLE Transaction (
    id INTEGER PRIMARY KEY,
    transaction_type TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id)
);