import gdown

url = 'https://drive.google.com/file/d/1cNfWe-F1cyN2Fcu7l9pXNFeVnhKKl09I/view?usp=sharing'
output = 'models/model.h5'
gdown.download(url, output, quiet=False, fuzzy=True)

for i in range(10):
    print("teste download")