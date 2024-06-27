import sqlite3
import json
from hashing import argon_hash
from new_user import add_user

con = sqlite3.connect("userinfo.db")  # Connection to the local database
cur = con.cursor()  # Allows execution of SQL queries

#cur.execute("CREATE TABLE ID(username, password)")

def new_user():
    user, un_hashed_password = add_user()
    hashed_password = argon_hash(un_hashed_password)

    # Insert the user and hashed password into the database using parameterized query
    cur.execute("INSERT INTO ID (username, password) VALUES (?, ?)", (user, hashed_password))
    con.commit()

def show_user_data():

    cur.execute("SELECT username, password FROM ID")
    data = cur.fetchall()
    # Print fetched usernames
    for vals in data :
        print(vals)

def database_to_dict():
    # Tuples of user, passwords in database
    cur.execute("SELECT username, password FROM ID")
    db = cur.fetchall()
    USER_DICT = dict((user, password) for user, password in db)
    return USER_DICT



user = database_to_dict()
with open("user.json", "w") as outfile:
    json.dump(user, outfile)

# Close the database connection
con.close()