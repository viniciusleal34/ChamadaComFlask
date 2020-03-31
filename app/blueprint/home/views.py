from . import home
from app import db
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from app.models.Turma import Turma
from app.models.Student import Student
from app.models.AlunoPresentes import AlunosPresentes
from app.api.Treinamento import Treinamento
from app.api.Reconhecimento import Reconhecimento
import os

UPLOAD_FOLDER_DESCRITOR = os.path.join(os.getcwd(), 'app', 'static', 'Descritor')
UPLOAD_FOLDER_INDICE = os.path.join(os.getcwd(), 'app', 'static', 'indice')
UPLOAD_FOLDER_IA = os.path.join(os.getcwd(), 'app', 'static', 'IA')

@home.route("/home", methods=['GET', 'POST'])
def index():
    turma_id = request.values.get("turma")
    if turma_id is None:
        turma_id = 1
    name_curso = db.turmas.find_one({'_id': int(turma_id)
        })

    turmas = db.turmas.find({'user_id': current_user.id
        })

    t = db.turmas.find_one({'user_id': current_user.id
        })


    student = db.students.find({'turma_id': int(turma_id)
        })
  
    return render_template('index.html', student = student, turmas = turmas, name_curso= name_curso)



@home.route("/presenca", methods=['GET', 'POST'])
def alunosPresentes():

    turma_id = request.values.get("turma")
    reconhecimento = db.turmas.find_one({'_id': int(turma_id)
        })
    r = Reconhecimento(UPLOAD_FOLDER_IA + "/shape.dat",UPLOAD_FOLDER_IA + "/dlib_face.dat",UPLOAD_FOLDER_IA + "/img","*.jpg",UPLOAD_FOLDER_INDICE +"/" +reconhecimento['indice_name'],UPLOAD_FOLDER_DESCRITOR +"/"+reconhecimento['descritor_name'])
    r.Reconhecer()
    studentes = db.students.find({'turma_id': int(turma_id)
        })
    presentes = r.getAlunosPresentes()

    for s in studentes:
            for i in range (len(presentes)):
                if s['ra'] in presentes[i]:
                    a = AlunosPresentes(s['ra'],True,s['name'], turma_id)
                    a.inserirDados()
                else:
                    a = AlunosPresentes(s['ra'],False,s['name'], turma_id)
                    a.inserirDados()
    return redirect(url_for('home.presents'))


@home.route("/presents", methods=['GET', 'POST'])
def presents():
    turma_id = request.values.get("turma")
    if turma_id is None:
        turma_id = 1
    name_curso = db.turmas.find_one({'_id': int(turma_id)
        })

    turmas = db.turmas.find({'user_id': current_user.id
        })
    print(turma_id)
    t = db.turmas.find_one({'user_id': current_user.id
        })

    print(turma_id)
    student = db.alunospresentes.find({'turma_id': int(turma_id)
        })

    return render_template('index.html', student = student, turmas = turmas, name_curso= name_curso)