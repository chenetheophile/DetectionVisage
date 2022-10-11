from tkinter.font import names
import cv2
import dlib
import numpy as np
from imutils import face_utils
import os
import ntpath
import sys
import getopt
import glob
import time
def lectureArgument(argv):
    """
    Définit les arguments par défaut et les remplacent ensuite par les arguments passés à la commande.
    """
    root=os.path.dirname(os.path.realpath(__file__))
    try:
        opts, args = getopt.getopt(argv,"hs:",["show_face="])
        show=False
    except getopt.GetoptError as e:
        print( 'facial_recognition.py -s <show_face>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print( 'facial_recognition.py -s <show_face>')
            sys.exit()
        elif opt in ("-s", "--show_face"):
            show=True
    return show


def detectVisage(args):
    show=lectureArgument(args)
    nb_essai=0
    name="Unknown"
    face_to_encode_path=os.path.dirname(os.path.realpath(__file__))+'/../DetectionVisage/known_faces/'
    files = [file_ for file_ in glob.glob(face_to_encode_path+'/*.jpg')]

    for file_ in glob.glob(face_to_encode_path+'/*.png'):
        files.append(file_)
    if len(files)==0:
        raise ValueError('No faces detect in the directory: {}'.format(face_to_encode_path))
    known_face_names = [os.path.splitext(ntpath.basename(file_))[0] for file_ in files]

    known_face_encodings = []
    for file_ in files:
        image = cv2.imread(file_)
        face_encoded = encode_face(image)[0][0]
        known_face_encodings.append(face_encoded)
    video_capture = cv2.VideoCapture(0)
    _, frame = video_capture.read()
    name=easy_face_reco(frame, known_face_encodings, known_face_names,show)
    while nb_essai<3 and name=="Unknown":
        nb_essai+=1
        if name=="Unknown":
            time.sleep(1)
        name=easy_face_reco(frame, known_face_encodings, known_face_names,show)
    if show:
        cv2.imshow('Easy Facial Recognition App', frame)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
    video_capture.release()
    return name

def transform(image, face_locations):
    coord_faces = []
    for face in face_locations:
        rect = face.top(), face.right(), face.bottom(), face.left()
        coord_face = max(rect[0], 0), min(rect[1], image.shape[1]), min(rect[2], image.shape[0]), max(rect[3], 0)
        coord_faces.append(coord_face)
    return coord_faces


def encode_face(image):
    face_locations = face_detector(image, 1)
    face_encodings_list = []
    landmarks_list = []
    for face_location in face_locations:
        # DETECT FACES
        shape = pose_predictor_68_point(image, face_location)
        face_encodings_list.append(np.array(face_encoder.compute_face_descriptor(image, shape, num_jitters=1)))
        # GET LANDMARKS
        shape = face_utils.shape_to_np(shape)
        landmarks_list.append(shape)
    face_locations = transform(image, face_locations)
    return face_encodings_list, face_locations, landmarks_list


def easy_face_reco(frame, known_face_encodings, known_face_names,show):
    name="Unknown"
    rgb_small_frame = frame[:, :, ::-1]
    # ENCODING FACE
    face_encodings_list, face_locations_list, landmarks_list = encode_face(rgb_small_frame)
    face_names = []
    for face_encoding in face_encodings_list:
        if len(face_encoding) == 0:
            return np.empty((0))
        # CHECK DISTANCE BETWEEN KNOWN FACES AND FACES DETECTED
        vectors = np.linalg.norm(known_face_encodings - face_encoding, axis=1)
        tolerance = 0.6
        result = []
        for vector in vectors:
            if vector <= tolerance:
                result.append(True)
            else:
                result.append(False)
        if True in result:
            first_match_index = result.index(True)
            name= known_face_names[first_match_index]
    if show:
        for (top, right, bottom, left), name in zip(face_locations_list, face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 30), (right, bottom), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (left + 2, bottom - 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

        for shape in landmarks_list:
            for (x, y) in shape:
                cv2.circle(frame, (x, y), 1, (255, 0, 255), -1)
    return name
if __name__=="__main__":
    root=os.path.dirname(os.path.realpath(__file__))
    pose_predictor_68_point = dlib.shape_predictor(root+"/pretrained_model/shape_predictor_68_face_landmarks.dat")
    # pose_predictor_5_point = dlib.shape_predictor("pretrained_model/shape_predictor_5_face_landmarks.dat")
    face_encoder = dlib.face_recognition_model_v1(root+"/pretrained_model/dlib_face_recognition_resnet_model_v1.dat")
    face_detector = dlib.get_frontal_face_detector()
    print(detectVisage(sys.argv[1:]))
    # detectVisage(sys.argv[1:])