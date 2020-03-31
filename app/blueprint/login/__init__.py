from flask import Blueprint

login = Blueprint('main', __name__)

from . import views