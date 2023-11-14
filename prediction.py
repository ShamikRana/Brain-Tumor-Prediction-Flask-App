import cv2
import numpy as np
from keras.models import load_model

image_size = 299
labels = ["glioma_tumor", "no_tumor", "meningioma_tumor", "pituitary_tumor"]

model = load_model('model.h5')

def preprocess_image(image_path, image_size):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (image_size, image_size))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def predict_tumor_class(model, image_path, labels):
    image = preprocess_image(image_path, image_size)
    prediction = model.predict(image)
    predicted_class = labels[np.argmax(prediction)]
    confidence = np.max(prediction) * 100
    return predicted_class, confidence
