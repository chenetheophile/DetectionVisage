"""

Ce fichier utiliser la bibliothèque face-recogntion.

dataset entrainé a placer les landmarks, encoder les résultats et ressortir le nom de l'image enregistré

Utilise un modèle cnn de la librairie dlib pré-entrainer pour tracer les landmarks

Detecte les visgae grace à un hog et un cnn 

install:
    pip install face-recognition

"""

import face_recognition
image = face_recognition.load_image_file("../DetectionVisage\img_complete.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)