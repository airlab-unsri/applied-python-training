import requests
import tensorflow as tf
from tensorflow import keras

# Import the Fashion MNIST dataset
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# scale the values to 0.0 to 1.0
train_images = train_images / 255.0
test_images = test_images / 255.0

# reshape for feeding into the model
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)


url = "http://localhost:8000"
req = tf.constant(test_images[:1], dtype=tf.float32)

resp = requests.post(f"{url}/predict", json={"instances": req.numpy().tolist()}).json()
print(resp)
