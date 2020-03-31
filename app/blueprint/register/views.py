from . import register
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app.models.User import User


@register.route("/register", methods=['GET', 'POST'])
def registrar():

    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        nome = request.form.get("nome")
        if nome and email and password and username:
            user = User(username,password,nome,email)
            user.inserirDados()
        #     db.session.add(user)
        #     db.session.commit()
        return  render_template('login.html')
    return render_template('register.html')
