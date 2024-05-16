CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY,
    username TEXT,
    title TEXT,
    content TEXT,
    FOREIGN KEY (username) REFERENCES users(username)
);


