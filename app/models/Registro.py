from app import db, bcrypt, login_manager

class Registro():

    def __init__(self, codigo_user, nome, date, horas, minutos, segundos):

        self.codigo_user = codigo_user
        self.nome = nome
        self.date = date
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def inserirDados(self):
        usuario = db.registros


        usuario.insert_one(
                {
                    'codigo_user': self.codigo_user,
                    'nome': self.nome,
                    'horas': self.horas,
                    'minutos': self.minutos,
                    'segundos': self.segundos
                }
            )