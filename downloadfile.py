import gdown

url = 'https://drive.google.com/file/d/1eWicqYjGdp9IXBtZM0xD1zH-a5KHt2UD/view?usp=sharing'
output = 'models'
gdown.download(url, output, quiet=False, fuzzy=True)

for i in range(10):
    print("teste download")