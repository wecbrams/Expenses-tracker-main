import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the data
x_train = x_train.astype("float32") \ 255.0
x_test = x_test.astype("float32") \ 255.0

# Reshape to add channel dimension (needed for ImageDataGenerator)
x_train = np.expand_dims(x_train, axis=-1)  # shape: (num_samples, 28, 28, 1)
x_test = np.expand_dims(x_test, axis=-1)

# Data Augmentation
datagen = ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1
)
datagen.fit(x_train)

# Build the model
model = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Flatten(),
    layers.Dense(128),
    layers.LeakyReLU(alpha=0.1),
    layers.Dense(64),
    layers.LeakyReLU(alpha=0.1),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='rmsprop',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(datagen.flow(x_train, y_train, batch_size=32), epochs=10)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")

# Make predictions
predictions = model.predict(x_test)

# Display the first image and prediction
plt.imshow(x_test[0].reshape(28, 28), cmap=plt.cm.binary)
plt.title(f"Predicted: {np.argmax(predictions[0])}")
plt.axis("off")
plt.show()
