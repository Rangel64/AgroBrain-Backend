import cv2
import numpy as np
import scipy.fftpack as fp
from tensorflow import keras
import pandas as pd
from GeradorDeIndices import EstimadorDeIndicesInfraRed as IF

def rede (nRed,nGreen,nBlue,gli,savi,mpri) :
    
    print('Rede neural analisando a imagem')
    
    entrada = []
    entrada.append(nRed)
    entrada.append(nGreen)
    entrada.append(nBlue)
    entrada.append(gli)
    entrada.append(savi)
    entrada.append(mpri)

    df = pd.DataFrame(entrada)
    
    array = np.array(df)
    array = np.transpose(array)
    
    df2 = pd.DataFrame(array)
    
    model = keras.models.load_model('models/model_teste_7_keras_nadam_11relu_linear_1200neur_Dropout_0.100000_100000epocs_patience_150.h5')
    
    return  model.predict(df2)

def result(imageBytes):
    
    image = cv2.imdecode(np.frombuffer(imageBytes,np.uint8),1)
    (nRed,nGreen,nBlue,gli,savi,mpri) = IF().calculoIndicesRNA(image)

    result = rede(nRed,nGreen,nBlue,gli,savi,mpri)
    print('Massa estimada: ' + str(result[0][0]))
    
    return result[0][0]






                                                                                        













