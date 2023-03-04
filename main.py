from flask import Flask, request, jsonify
import json
import base64
import Estimador
import gdown


app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])


def index():
    global reponse
    
    if(request.method == 'POST'):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        decodeString = request_data['image']
        imageBytes = base64.b64decode((decodeString))
        numeroDeAnimais = Estimador.result(imageBytes)
        return jsonify({'response': str(numeroDeAnimais)})
    
    return "<h1>Hello World</h1>"  
        
if(__name__ == "__main__"):
    url = 'https://drive.google.com/file/d/1mhk3M-qOR2tr22HHMe5ajKbl7k8EeUa2/view?usp=share_link'
    output = 'models/model_teste_7_keras_nadam_11relu_linear_1200neur_Dropout_0.100000_100000epocs_patience_150.h5'
    gdown.download(url, output, quiet=False)
    app.run(host = '0.0.0.0',port=5000,debug=True)

