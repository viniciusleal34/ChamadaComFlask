from Treinamento import Treinamento
from Reconhecimento import Reconhecimento
from Testando import Testando
import dlib
import cv2
import os
import glob
import pickle as cPickle
import numpy as np
# a = Treinamento("recursos/recursos/shape_predictor_68_face_landmarks.dat","recursos/recursos/dlib_face_recognition_resnet_model_v1.dat","recursos/vini","*.jpg")

# a.treino()
a = Reconhecimento("recursos/recursos/shape_predictor_68_face_landmarks.dat","recursos/recursos/dlib_face_recognition_resnet_model_v1.dat","recursos/img","*.jpg","recursos/indices_rn_vini.pickel","recursos/descritores_rn_vini.npy")
a.Reconhecer()

