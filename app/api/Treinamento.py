# -*- coding: utf-8 -*-
import dlib
import cv2
import os
import glob
import pickle as cPickle
import numpy as np


#criando detectores
class Treinamento:
    def __init__(self, detectorPontos, reconhecimentoFacial, caminho, formato):
        self.detectorFace = dlib.get_frontal_face_detector()
        self.detectorPontos = dlib.shape_predictor(detectorPontos)
        self.reconhecimentoFacial = dlib.face_recognition_model_v1(reconhecimentoFacial)
        self.indice = {}
        self.idx = 0
        self.descritoresFaciais = None
        self.caminho = caminho
        self.formato = formato

    def treino(self):
        for arquivo in glob.glob(os.path.join(self.caminho, self.formato)):
            imagem = cv2.imread(arquivo)
            facesDetectadas = self.detectorFace(imagem,1)
            numeroFacesDetectadas = len(facesDetectadas)


            if numeroFacesDetectadas >  1:
                print("Há mais de uma face na imagem {}".format(arquivo))
                exit(0)
            elif numeroFacesDetectadas < 1:
                print("Não há faces detectadas no arquivo {}".format(arquivo))
                exit(0)
            for face in facesDetectadas:
                pontosFaciais = self.detectorPontos(imagem, face)
                descritoresFacial = self.reconhecimentoFacial.compute_face_descriptor(imagem, pontosFaciais)
                listaDescritorFacial = [df for df in descritoresFacial]
                npArrayDescritorFacial = np.asarray(listaDescritorFacial, dtype=np.float64)
                npArrayDescritorFacial = npArrayDescritorFacial[np.newaxis, :]
                if self.descritoresFaciais is None:
                    self.descritoresFaciais = npArrayDescritorFacial
                else:
                    self.descritoresFaciais = np.concatenate((self.descritoresFaciais, npArrayDescritorFacial),axis=0)
                self.indice[self.idx] = arquivo
                self.idx += 1

        np.save("recursos/descritores_rn_vini.npy", self.descritoresFaciais)
        with open("recursos/indices_rn_vini.pickel", 'wb') as f:
            cPickle.dump(self.indice,f)
#cv2.destroyAllWindows()

