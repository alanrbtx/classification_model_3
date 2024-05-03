from flask import Flask, request
import pickle
from skimage import io
from skimage.transform import resize
from skimage.color import rgb2gray
import redis
import os
import os
from dotenv import load_dotenv
import hvac

pkl_path = '/classification/neigh.pkl'
def load_pickle(file_path):
    neigh = pickle.load(open(file_path, 'rb'))
    return neigh

def predict_image(file_path):
    image = io.imread(file_path)
    if len(image.shape) == 4:
        image = image.squeeze(0)
    image = rgb2gray(resize(image, (200,200)))
    image = image.reshape(1, -1)

    neigh = load_pickle(pkl_path)
    res = neigh.predict(image)[0]
    if res == 0:
        print("MODEL PREDICTION: CAT")
        return {"result": "cat"}
    else:
        print("MODEL PREDICTION: DOG")
        return {"result": "dog"}

app = Flask(__name__)

@app.route('/get_test_prediction', methods=['GET'])
def get_test_result():
    res = predict_image("/dataset/PetImages/Cat/3004.jpg")
    return res

@app.route('/get_real_prediction', methods=['POST'])
def get_real_result():
    res = predict_image(request.files["media"])

    client = hvac.Client(
         url='http://host.docker.internal:8200',
         token='hvsvio2dl8SxHJU83uFk8O8JGGE',
     )

    client.is_authenticated()

    read_response = client.secrets.kv.read_secret_version(path='server')

    password=read_response['data']['data']['PASS']
    host=read_response['data']['data']['HOST']
    port=read_response['data']['data']['PORT']

    print(password, host, port)
    
    r = redis.Redis(host=host,
                    port=port,
                    db=0,
                    password=password)
    
    r.set(request.remote_addr, f"prediction: {res}")

    keys = r.keys()
    for key in keys:
        print(f"key: {key}", f"value: {r.get(key)}")
        print(10*"---")

    return res


class TestClass():
    def test_load_picke(self):
        assert load_pickle('/classification/neigh.pkl')

    def test_predict(self):
        assert predict_image('/dataset/PetImages/Cat/3004.jpg')

    
if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')