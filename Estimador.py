import cv2
import numpy as np
# import scipy.fftpack as fp
from tensorflow import keras
import pandas as pd
from GeradorDeIndices import EstimadorDeIndicesInfraRed as IF

def rede (nRed,nGreen,nBlue,hn,sn,vn,gli,savi,mpri) :
    
    print('Rede neural analisando a imagem')
    
    entrada = []
    entrada.append(nRed)
    entrada.append(nGreen)
    entrada.append(nBlue)
    entrada.append(hn)
    entrada.append(sn)
    entrada.append(vn)
    entrada.append(gli)
    entrada.append(savi)
    entrada.append(mpri)

    df = pd.DataFrame(entrada)
    
    array = np.array(df)
    array = np.transpose(array)
    
    df2 = pd.DataFrame(array)
    print(df2)
    
    model = keras.models.load_model('models/HSV_model_teste_4_keras_nadam_8selu_selu_350neur_Dropout_0.000000_100000epocs_patience_250.h5')
    
    return  model.predict(df2)

def result(imageBytes):
    
    image = cv2.imdecode(np.frombuffer(imageBytes,np.uint8),1)
    (nRed,nGreen,nBlue,hn,sn,vn,gli,savi,mpri) = IF().calculoIndicesRNA(image)

    result = rede(nRed,nGreen,nBlue,hn,sn,vn,gli,savi,mpri)
    resultCorrection =  result[0][0] - result[0][0]*0.174
    print('Massa estimada bruta: ' + str(result[0][0]))
    print('Massa estimada corrigida: ' + str(resultCorrection))
    return resultCorrection






                                                                                        













