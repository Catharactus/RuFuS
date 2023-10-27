from PIL import Image
import numpy as np
import pytorch as torch

device = torch.device(“cuda” if torch.cuda.is_available() else “cpu”)

def GetDepthImage():
    #load the image


    #convert the image in a numpy table 

    #Send the image to midas with the right settings

    #get the prediction from midas in a png 

    #download the png directly in a floder
    pass

