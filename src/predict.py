import pickle
from skimage import io
from skimage.transform import resize
from skimage.color import rgb2gray


pkl_path = '../experiments/neigh.pkl'
def load_pickle(file_path):
    neigh = pickle.load(open(file_path, 'rb'))
    return neigh

# pytest
def test_load_picke():
    assert load_pickle('../experiments/neigh.pkl')

def predict_image(file_path):
    image = io.imread(file_path)
    if len(image.shape) == 4:
        image = image.squeeze(0)
    image = rgb2gray(resize(image, (200,200)))
    image = image.reshape(1, -1)

    neigh = load_pickle(pkl_path)
    res = neigh.predict(image)[0]
    if res == 0:
        print("Cat")
    else:
        print("Dog")

if __name__=='__main__':
    predict_image("../data/PetImages/cat/3004.jpg")