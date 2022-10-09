import os

if __name__=="__main__":
    root=os.path.dirname(os.path.realpath(__file__))
    os.system("python "+root+"/../DetectionVisage/detectionVisage.py")
    os.system("python "+root+"/../Inference/inference.py "+root+'/../DetectionVisage/img_complete.jpg')