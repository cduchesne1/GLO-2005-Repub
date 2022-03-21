CREATE TABLE IF NOT EXISTS users(
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL
);

INSERT INTO users(name, username) VALUES('admin', 'admin');