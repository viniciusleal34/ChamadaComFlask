from app import db, bcrypt, login_manager
class Presence():

    def __init__(self, subject_id, students_id, aula_id, presenca):
        self.subject_id = subject_id
        self.students_id = students_id
        self.aula_id = aula_id
        self.presenca = presenca

    def inserirDados(self):
        usuario = db.aulas
        usuario.insert_one(
                {
                    '_id':  int(usuario.find().count()) + 1,
                    'subject_id': self.subject_id,
                    'aula_id': self.aula_id,
                    'students_id': self.students_id,
                    'presenca': self.presenca
                }
            )

