import cv2
import numpy as np

class EstimadorDeIndicesInfraRed:
    
    def calculoIndicesInfraRed(self,red, green, blue):
        
        gli = (2*green-red-blue)/(2*green+red+blue)
        savi = 1.5*((green-red)/(green+red+0.5))
        mpri = (green-red)/(green+red)
    
        return gli, savi, mpri
    
    
    def calculoIndicesRNA(self,image):
        
        imageSHV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        (imageBlue,imageGreen,imageRed) = cv2.split(image)
        
        h, s, v = cv2.split(imageSHV)
        
        hm = np.mean(h)
        sm = np.mean(s)
        vm = np.mean(v)
        
        Green = np.mean(imageGreen)
        Red = np.mean(imageRed)
        Blue = np.mean(imageBlue)
        
        nRed = Red/(255)
        nGreen = Green/(255)
        nBlue = Blue/(255)
        
        hn = hm/255
        sn = sm/255
        vn = vm/255
        
        (gli,savi,mpri) = self.calculoIndicesInfraRed(Red,Green,Blue)
         
        return (nRed,nGreen,nBlue,hn,sn,vn,gli,savi,mpri)
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    