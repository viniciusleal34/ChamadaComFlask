from . import login
from flask import render_template, request, redirect, url_for
from app.models.User import User
from app import app, db, bcrypt
from flask_login import login_user, logout_user

@login.route('/',  methods=['GET', 'POST'])
def entrar():

    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")


        u = db.users.find_one({
         'username': username
         }

        )
        if u:
            user=User(u['username'], u['password'], u['name'], u['email'])

        if not u or not bcrypt.check_password_hash(u['password'],password):

            return render_template("login.html")
        login_user(user)

        return redirect(url_for("home.index"))
    return render_template('login.html')


@login.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.entrar'))
