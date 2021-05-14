# tornado_POC
A  POC on tornado frame work

# Create virtual enviornment:
    python3 -m venv venv
    python3 venv/bin/activate
    pip install -r requirements.txt

# Create Data base:
    $sudo su postgres
    $psql
    postgres=# CREATE DATABASE tornado_poc
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;
    postgres=# \q
    exit

# Create a table:
    CREATE TABLE accounts (
        user_id serial PRIMARY KEY,
        username VARCHAR ( 50 ) UNIQUE NOT NULL,
        password VARCHAR ( 50 ) NOT NULL,
        email VARCHAR ( 255 ) UNIQUE NOT NULL,
        created_on TIMESTAMP,
        last_login TIMESTAMP);
    
    Insert data in this table