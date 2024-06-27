from flask import Flask, render_template, request
import database as db
from hashing import argon_hash, ph
import json

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def login_page():  # put application's code here
    if request.method == "POST":

        init_data = open("user.json")
        data_dict = json.load(init_data)

        # Retrieval of form entries used inside of the form
        form_username = request.form.get("username")
        form_password = request.form.get("password")

        # Checks if username exists in the database
        if form_username in data_dict:
            print("Print Key exists!")
        else:
            print("Key not found")

        # Hashing of password using argon2 encryption
        hashed_password = argon_hash(form_password)
        is_valid = ph.verify(hashed_password, form_password)
        print(is_valid)





    return render_template('login.html')


if __name__ == '__main__':
    app.run()
