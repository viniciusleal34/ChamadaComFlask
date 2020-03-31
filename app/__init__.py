from flask import Flask
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)


app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret'

client = MongoClient("mongodb+srv://viniciusleal34:123eamm9@cluster0-x1yn9.mongodb.net/test?retryWrites=true&w=majority")
db = client.Fatec


from app.blueprint.login import login
app.register_blueprint(login)

from app.blueprint.cadastro import cadastro
app.register_blueprint(cadastro)

from app.blueprint.home import home
app.register_blueprint(home)

from app.blueprint.register import register
app.register_blueprint(register)


from app.models import AlunoPresentes,Aula, Presence, Registro,Student,Subject,Turma,User
from app.controllers import default