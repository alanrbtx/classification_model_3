import numpy as np
from skimage import io
from skimage.transform import resize
from skimage.color import rgb2gray
from sklearn.neighbors import KNeighborsClassifier
import pickle
import numpy as np
import os
import json
from preprocess import PrepareDataset
from dvclive import Live
import configparser

path_to_data = "../data/PetImages/"

def prepare_dataset(path_to_data):
    x_train, y_train = PrepareDataset(path_to_data + "Cat/", path_to_data + "Dog/").preprocess_train()
    x_test, y_test = PrepareDataset(path_to_data + "Cat/", path_to_data + "Dog/").preprocess_test()

    x_train = x_train.reshape(x_train.shape[0], -1)
    x_test = x_test.reshape(x_test.shape[0], -1)
    print("DATA PREPARED")

    return x_train, y_train, x_test, y_test

x_train, y_train, x_test, y_test = prepare_dataset(path_to_data)


hyperparam_config = configparser.ConfigParser()
hyperparam_config.read("../config.ini")

# Access the values
num_neighbors = hyperparam_config.get("hyperparam", "num_neighbors")
neigh = KNeighborsClassifier(n_neighbors=int(num_neighbors), n_jobs=-1)

def generate_exp_token():
        token = np.random.randint(low=0, high=100, size=10)
        str_token = ''
        for i in token:
            str_token += str(i)
        return str_token


class TestClass():
    def test_prepare_dataset(self):
         assert prepare_dataset(path_to_data)

    def test_model_initialization(self):
         assert KNeighborsClassifier(n_neighbors=5, n_jobs=-1)

    def test_generate_token(self):
         assert generate_exp_token()


if __name__=='__main__':
    with Live() as live:
        neigh.fit(x_train,y_train)
        print("MODEL LOADED")

        print("START TRAINING")
        score_train = neigh.score(x_train, y_train)
        print("Training score: {:.2f}%".format(score_train*100))

        score_test = neigh.score(x_test, y_test)
        print("Test score: {:.2f}%".format(score_test*100))

        #live.log_metric(name="Training score", val=score_train)
        #live.log_metric(name="Test score", val=score_test)

        token = generate_exp_token()
        # os.mkdir(f"experiments/exp_{token}")

        # save pkl model
        with open(f'../experiments/neigh.pkl', 'wb') as knnPickle:
            res = pickle.dump(neigh, knnPickle)
            pkl_hash = res.__hash__()
            print("MODEL SAVED")

        # save config
        config = {
            "n_neighbors": 5,
            "path_to_data": path_to_data,
            "model_type": "KNeighborsClassifier",
            "pkl_hash": pkl_hash
        }

        with open(f"../experiments/config.json", "w") as json_file:
            json.dump(config, json_file)

        # save metrics
        metrics = {
            "score train": score_train, 
            "score_test": score_test
        }
        with open(f"../experiments/metrics.json", "w") as json_file:
            json.dump(metrics, json_file)