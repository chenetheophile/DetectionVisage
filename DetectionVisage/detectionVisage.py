import pathlib
import cv2
import time
import os

if __name__=="__main__":
    cascade_path=pathlib.Path(cv2.__file__).parent.absolute() /"data/haarcascade_frontalface_default.xml"

    clf=cv2.CascadeClassifier(str(cascade_path))

    camera=cv2.VideoCapture(0)
    nb_essai=0

    root=os.path.dirname(os.path.realpath(cv2.__file__))


    while nb_essai<3:
        _,frame=camera.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=clf.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=1,
            minSize=(30,30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x,y,width,height) in faces:
            # cv2.rectangle(frame,(x,y),(x+width,y+height),(255,255,0),2)
            cv2.imwrite(root+"/img_complete.jpg",frame)
            subimage=frame[y:y+height,x:x+width]
            cv2.imwrite(root+"./img_only_face.jpg",subimage)
        nb_essai+=1
        time.sleep(1)
    camera.release()