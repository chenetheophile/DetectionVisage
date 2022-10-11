import os

if __name__=="__main__":
    root=os.path.dirname(os.path.realpath(__file__))
    os.system("python "+root+"/../DetectionVisage/detectionVisage.py")
<<<<<<< HEAD
    os.system("python "+root+"/../Inference/facial_recognition.py "+root+'/../DetectionVisage/img_complete.jpg')
=======
    os.system("python "+root+"/../Inference/inference.py "+root+'/../DetectionVisage/img_complete.jpg')
>>>>>>> parent of da5166c4 (Merge branch 'main' of https://github.com/chenetheophile/DetectionVisage)
