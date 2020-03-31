# from flask import render_template, request, redirect, url_for
# from app import app, db
# import os
# import pickle
# #from flask_login import login_user, logout_user, current_user
# from werkzeug.utils import secure_filename
# from app.models.tablesMongo import User
# # from werkzeug.security import generate_password_hash, check_password_hash



# @app.route("/home", methods=['GET', 'POST'])
# def index():
#     # subject = Subject.query.filter_by(user_id=current_user.id).first()
#     # materias =  Subject.query.filter_by(user_id=current_user.id)
#     # turmas = Turma.query.filter_by(user_id=current_user.id)

#     # student = Student.query.filter_by(subject_id=subject.id)
#     return render_template('index.html')


# # @app.route("/")
# # def login():
# #     return render_template('login.html')
    


# @app.route("/register", methods=['GET', 'POST'])
# def register():

#     if request.method == 'POST':
#         username = request.form.get("username")
#         password = request.form.get("password")
#         email = request.form.get("email")
#         nome = request.form.get("nome")
#         if nome and email and password and username:
#             user = User(username,password,nome,email)
#             user.inserirDados()
#         #     db.session.add(user)
#         #     db.session.commit()
#         return  render_template('login.html')
#     return render_template('register.html')

    
    



