import gdown

url = 'https://drive.google.com/file/d/1mhk3M-qOR2tr22HHMe5ajKbl7k8EeUa2/view?usp=sharing'
output = 'models/model_teste_7_keras_nadam_11relu_linear_1200neur_Dropout_0.100000_100000epocs_patience_150.h5'
gdown.download(url, output, quiet=False, fuzzy=True)

for i in range(10):
    print("teste download")