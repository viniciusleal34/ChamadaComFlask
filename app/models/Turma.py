from app import db, bcrypt, login_manager
class Turma():

    def __init__(self, subject_id, disciplina, turno, curso, indice_name, descritor_name, user_id,):

        self.subject_id = subject_id
        self.disciplina = disciplina
        self.turno = turno
        self.curso = curso
        self.indice_name = indice_name
        self.descritor_name = descritor_name
        self.user_id = user_id

    def inserirDados(self):
        usuario = db.turmas


        usuario.insert_one(
                {
                    '_id': int(usuario.find().count()) + 1,
                    'subject_id': self.subject_id,
                    'disciplina': self.disciplina,
                    'turno': self.turno,
                    'curso': self.curso,
                    'indice_name': self.indice_name,
                    'user_id': self.user_id,
                    'descritor_name': self.descritor_name,
                }
            )