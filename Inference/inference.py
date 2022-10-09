from PIL import Image
from tensorflow.keras.preprocessing.image import array_to_img,img_to_array
from tensorflow.keras.models import load_model
from tensorflow.io import read_file,decode_image
from tensorflow import expand_dims
from tensorflow.dtypes import uint8
import numpy as np
import sys,os,getopt

def detectVisage(args):
    try:
        img,model_path=lectureArgument(args)
    except:
        return "Erreur dans la lecture d'argument"
    class_names=["Chef_projet","Expert_IA","WebDesigner","Autre"]
    model = load_model(model_path)
    img = decode_image(read_file(img), channels=3,dtype=uint8)
    img=Reformat_Image(img,450)
    img = expand_dims(img, axis=0)
    prediction=model.predict(img,verbose=0)
    indexOfClass=np.argmax(prediction,axis=1)[0]
    return {'class':class_names[indexOfClass],'score':float(prediction[0][indexOfClass])}
    
def lectureArgument(argv):
    """
    Définit les arguments par défaut et les remplacent ensuite par les arguments passés à la commande.
    """
    root=os.path.dirname(os.path.realpath(__file__))
    img_path=root+"../DetectionVisage/img.jpg"
    model_path=root+'/modelDetectionVisage.h5'
    try:
        opts, args = getopt.getopt(argv,"hi:m:",["img_path=","model_path"])
    except getopt.GetoptError as e:
        print( 'inference.py -i <img_path> -m <model_path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print( 'inference.py -i <img_path> -m <model_path>')
            sys.exit()
        elif opt in ("-i", "--img_path"):
            img_path=arg
        elif opt in ("-m","--model_path"):
            model_path=arg
    return img_path,model_path
        

def Reformat_Image(image,size):
    image = array_to_img(image)
    image_size = image.size
    width = image_size[0]
    height = image_size[1]
    if(width != size or height!=size):
        bigside = width if width > height else height
        
        background = Image.new('RGB', (bigside, bigside), (255, 255, 255))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))

        background.paste(image, offset)
        return img_to_array(background)

if __name__=="__main__":
    detectVisage(sys.argv[1:])