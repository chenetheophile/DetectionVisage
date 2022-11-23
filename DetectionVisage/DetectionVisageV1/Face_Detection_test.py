import os
import time
import uuid
import cv2

#https://www.youtube.com/watch?v=N_W4EYtsa10

#IMAGES_PATH = "../Data_images/images/"
import random
root=os.path.dirname(os.path.realpath(cv2.__file__))
#IMAGES_PATH = "../DetectionVisage/Data_images/images/"
#IMAGES_PATH = "/DetectionVisage/Data_images/images/"
IMAGES_PATH = "C:/Users/Meatisdelicious/Documents/5_Cours_ingé3/7_Projet_Fin_Annee/DetectionVisage/Data_images/images/"

number_images=1
cap = cv2.VideoCapture(0) #gaffe au port de la camera mdrrr
for imgnum in range(number_images):
    time.sleep(5)
    print('Collecting image {}'.format(imgnum))
    ret,frame =cap.read() #captures the frame and allows us to write it down
    print("ret:",ret)
    imgname = os.path.join(IMAGES_PATH,f'{imgnum+random.randint(0,100)}wasa.jpg')
    print(imgname)
    fwrite=cv2.imwrite(imgname,frame)
    print(fwrite)
    f = open(imgname, mode='w') # if this work, the writing will work...
    time.sleep(5)
    cv2.imshow('frame',frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()