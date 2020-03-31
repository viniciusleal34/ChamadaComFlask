from app import db, bcrypt, login_manager


class AlunosPresentes():

    def __init__(self, ra, presente, name, turma_id):

        self.ra = ra
        self.name = name
        self.presente = presente
        self.turma_id = turma_id

    def inserirDados(self):
        usuario = db.alunospresentes


        usuario.insert_one(
                {
                    'ra': self.ra,
                    'name': self.name,
                    'presente': self.presente,
                    'turma_id': self.turma_id
                }
            )

