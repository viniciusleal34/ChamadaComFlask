from app import db, bcrypt, login_manager

class Subject():

    def __init__(self,  name, user_id):
        self.name = name
        self.user_id = user_id

    def inserirDados(self):
        usuario = db.subjects
        usuario.insert_one(
                {
                    '_id': int(usuario.find().count()) + 1,
                    'name': self.name,
                    'user_id': self.user_id,

                }
            )

class Student():

    def __init__(self, ra, name, turma_id):
        self.ra = ra
        self.name = name
        self.turma_id = turma_id

    def inserirDados(self):
        usuario = db.students
        exist = usuario.find_one({'ra': self.ra})
        usuario.insert_one(
                {
                    'ra': self.ra,
                    'name': self.name,
                    'turma_id': self.turma_id,
                }
            )

