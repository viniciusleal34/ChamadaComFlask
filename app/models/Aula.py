from app import db, bcrypt, login_manager
from datetime import date
class Aula():

    def __init__(self,  subject_id):
        self.subject_id = subject_id
        self.data =  date.today()

    def inserirDados(self):
        usuario = db.aulas
        usuario.insert_one(
                {
                    '_id':  int(usuario.find().count()) + 1,
                    'data': self.data,
                    'subject_id': self.subject_id,
                }
            )

