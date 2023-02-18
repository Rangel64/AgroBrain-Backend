import cv2
import numpy as np
import pandas as pd

class EstimadorDeIndicesInfraRed:
    
    def calculoIndicesInfraRed(self,red, green, blue):
        
        gli = (2*green-red-blue)/(2*green+red+blue)
        savi = 1.5*((green-red)/(green+red+0.5))
        mpri = (green-red)/(green+red+0.5)
    
        return gli, savi, mpri
    
    
    def calculoIndicesRNA(self,image):
        
        (imageBlue,imageGreen,imageRed) = cv2.split(image) 
        
        Green = np.mean(imageGreen)
        Red = np.mean(imageRed)
        Blue = np.mean(imageBlue)
        
        nRed = Red/(Red+Green+Blue)
        nGreen = Green/(Red+Green+Blue)
        nBlue = Blue/(Red+Green+Blue)
    
        
        (gli,savi,mpri) = self.calculoIndicesInfraRed(Red,Green,Blue)
         
        return (nRed,nGreen,nBlue,gli,savi,mpri)