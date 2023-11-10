import gdown

url = 'https://drive.google.com/file/d/1eWicqYjGdp9IXBtZM0xD1zH-a5KHt2UD/view?usp=sharing'
output = 'models/HSV_model_teste_4_keras_nadam_8selu_selu_350neur_Dropout_0.000000_100000epocs_patience_250.h5'
gdown.download(url, output, quiet=False, fuzzy=True)

for i in range(10):
    print("teste download")