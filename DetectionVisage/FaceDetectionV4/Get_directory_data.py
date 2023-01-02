import os
path=r"/home/meatisdelicious/DetectionVisage/DetectionVisage/FaceDetectionV4/input/face_recognition_dataset/Original_Images_more"
for root,dirs,files in os.walk(path):
    if dirs==[]:
        print(root+": "+str(len(files))+" files")

