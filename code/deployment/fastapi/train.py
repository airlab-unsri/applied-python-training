import os

import tensorflow as tf
from tensorflow import keras

print("TensorFlow version: {}".format(tf.__version__))

# Import the Fashion MNIST dataset
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# scale the values to 0.0 to 1.0
train_images = train_images / 255.0
test_images = test_images / 255.0

# reshape for feeding into the model
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

class_names = [
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle boot",
]

print("train_images.shape: {}, of {}".format(train_images.shape, train_images.dtype))
print("test_images.shape: {}, of {}".format(test_images.shape, test_images.dtype))

# Train and evaluate the model
model = keras.Sequential(
    [
        keras.layers.Conv2D(
            input_shape=(28, 28, 1),
            filters=8,
            kernel_size=3,
            strides=2,
            activation="relu",
            name="Conv1",
        ),
        keras.layers.Flatten(),
        keras.layers.Dense(10, name="Dense"),
    ]
)
model.summary()

testing = False
epochs = 5

model.compile(
    optimizer="adam",
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=[keras.metrics.SparseCategoricalAccuracy()],
)
model.fit(train_images, train_labels, epochs=epochs)
print("Model trained!")

# Fetch the Keras session and save the model
MODEL_DIR = "model"
version = 1
model_format = ".keras"
model_path = os.path.join(MODEL_DIR, str(version) + model_format)
print("model_path = {}\n".format(model_path))

tf.keras.models.save_model(
    model,
    model_path,
    overwrite=True,
    include_optimizer=True,
    save_format=None,
)
print("Model saved!")

# Test saved model
model = tf.keras.models.load_model(model_path)
print(model.summary())

sample_input = tf.constant(test_images[:1], dtype=tf.float32)
output = model(sample_input)
print(output)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print("\nTest accuracy: {}".format(test_acc))
