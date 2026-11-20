
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS KS_users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    username TEXT,
    email TEXT,
    city TEXT,
    zipcode TEXT,
    company_name TEXT
);

CREATE TABLE IF NOT EXISTS KS_posts (
    id INTEGER PRIMARY KEY,
    userId INTEGER,
    title TEXT,
    body TEXT,
    status TEXT,
    FOREIGN KEY (userId) REFERENCES KS_users(id)
);
