from . import cadastro
from flask import render_template, request, redirect, url_for
from app import app, db
import os
import pickle
from werkzeug.utils import secure_filename
from flask_login import current_user
from app.models.Turma import Turma
from app.models.Student import Student


UPLOAD_FOLDER_DESCRITOR = os.path.join(os.getcwd(), 'app', 'static', 'Descritor')
UPLOAD_FOLDER_INDICE = os.path.join(os.getcwd(), 'app', 'static', 'indice')


@cadastro.route("/cadastrar", methods=['GET', 'POST'])
def cadastrar():
    cont =0
    if request.method == 'POST':
        disciplica = request.form.get("disciplica")
        turno = request.form.get("turno")
        curso = request.form.get("curso")

        if request.files:
            alunos = request.files["alunos"]
            descritores = request.files["descritor"]
            savePath = os.path.join(UPLOAD_FOLDER_INDICE, secure_filename(alunos.filename))
            alunos.save(savePath)
            descritores.save( os.path.join(UPLOAD_FOLDER_DESCRITOR, secure_filename(descritores.filename)))
            alunos.close()
            descritores.close()
            aluno_arq = open(os.path.join(UPLOAD_FOLDER_INDICE, secure_filename(alunos.filename)),"rb")
            #descritores_arq=open(os.path.join(UPLOAD_FOLDER, secure_filename(descritores.filename)),"rb")
            estudante = pickle.load(aluno_arq)
            # descritores_gg = pickle.load(descritores_arq)
            indiceArq = alunos.filename
            descritor = descritores.filename
            subject = db.subjects.find_one({
         'name': disciplica
         }

        )
            user_id = current_user.id
            turma = Turma(subject['_id'],disciplica,turno,curso,indiceArq,descritor, user_id)
            turma.inserirDados()
            turma_id = db.turmas.count()
            # db.session.add(turma)
            # db.session.commit()

            for i in estudante:
                if len(estudante) > cont+3:
                    nome = estudante[cont].split("/")[2].split('.')[0]
                    ra = estudante[cont].split("/")[2].split('.')[1]
                    # turma_id = db.turmas.find_one({
                    # 'subject_id':subject['_id'],
                    # 'disciplica': disciplica,
                    # 'turno': turno,
                    # 'curso': curso,
                    # 'indice_name': indiceArq,
                    # 'user_id': current_user.id,
                    # 'descritor_name': descritor

                    #     }

                    # )
                    student = Student(ra, nome, int(turma_id))
                    student.inserirDados()
                    # db.session.add(student)
                    # db.session.commit()
    
                cont=cont+4
        
        return redirect(url_for('cadastro.materias'))

        
    return render_template("cadastro.html")

@cadastro.route("/cadastro")
def materias():
    # subject = Subject.query.filter_by(user_id=current_user.id)
    subject = db.subjects.find({
        'user_id': current_user.id
    })
    return render_template("cadastro.html", subject= subject)