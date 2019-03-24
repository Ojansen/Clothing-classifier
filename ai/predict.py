from __future__ import absolute_import, division, print_function

# TensorFlow and tf.keras
import keras
from keras.models import load_model
from keras.utils import CustomObjectScope
from keras.initializers import glorot_uniform
from skimage import io, transform, util
import matplotlib.pyplot as plt
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images / 255
test_images = test_images / 255

# the names to put into the plot
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
print(os.getcwd())


with CustomObjectScope({'GlorotUniform': glorot_uniform()}):
    model = load_model(os.path.join(os.getcwd(), 'ai/model/img-model.h5'))


def plot_image(i, predictions_array, true_label, img):
    fig = plt.figure()
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}%".format(class_names[predicted_label],
                                         100 * np.max(predictions_array)),
               color=color)
    fig.savefig("assets/grey_img_out.jpeg", quality=90, format="jpeg")


def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array[i], true_label[i]
    fig = plt.figure()
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')

    _ = plt.xticks(range(10), class_names, rotation=45)

    fig.savefig("assets/predict_graph.jpeg", quality=90, format="jpeg")


def input_image():

    np_image = io.imread('assets/image_to_predict.jpeg', as_grey=True)
    np_image = util.img_as_float64(np_image)
    np_image = util.invert(np_image)
    np_image = transform.resize(np_image, (28, 28))
    np_image = (np.expand_dims(np_image, 0))

    prediction_single = model.predict(np_image)
    plot_value_array(0, prediction_single, test_labels)
    plot_image(0, prediction_single, test_labels, np_image)
    return f"saved: {np_image}"
