import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.transform import resize
from skimage.color import rgb2gray


class PrepareDataset:
    def __init__(self, cats_path, dogs_path):
        super().__init__()
        self.cats_path = cats_path
        self.dogs_path = dogs_path
        
    
    def preprocess_train(self):
        x_train = []; y_train = []
        for i in range(0,2000):
            cat_image = io.imread(self.cats_path + '{}.jpg'.format(i))
            if len(cat_image.shape) == 4:
                cat_image = cat_image.squeeze(0)
            cat = rgb2gray(resize(cat_image, (200,200)))
            x_train.append(cat); y_train.append(0) #0-->'cat'
            
        for i in range(0,2000):
            dog_image = io.imread(self.dogs_path + '{}.jpg'.format(i))
            if len(dog_image.shape) == 4:
                dog_image = dog_image.squeeze(0)
            dog = rgb2gray(resize(dog_image, (200,200)))
            x_train.append(dog); y_train.append(1) #1-->'dog'
            
        x_train, y_train = np.asarray(x_train), np.asarray(y_train)
        print('x_train shape: ', x_train.shape, 'y_train shape: ', y_train.shape)
        return x_train, y_train
    

    def preprocess_test(self):
        x_test = []; y_test = []
        for i in range(2001, 3001):
            cat_image = io.imread(self.cats_path + '{}.jpg'.format(i))
            if len(cat_image.shape) == 4:
                cat_image = cat_image.squeeze(0)
            cat = rgb2gray(resize(cat_image, (200,200)))
            x_test.append(cat); y_test.append(0) #0-->'cat'
            
        for i in range(2001, 3001):
            dog_image = io.imread(self.cats_path + '{}.jpg'.format(i))
            if len(dog_image.shape) == 4:
                dog_image = dog_image.squeeze(0)
            dog = rgb2gray(resize(dog_image, (200,200)))
            x_test.append(dog); y_test.append(1) #1-->'dog'
            
        x_test, y_test = np.asarray(x_test), np.asarray(y_test)
        print('x_test shape: ',x_test.shape, 'y_test shape: ', y_test.shape)
        return x_test, y_test