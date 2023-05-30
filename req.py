import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import json
import requests
import tensorflow as tf
import cv2

def load_image_into_numpy_array(path):
    return np.array(Image.open(path))

PATH = './image3.jpg'


test_image = load_image_into_numpy_array(PATH)
reshaped_image = np.expand_dims(test_image, 0)
data = json.dumps({"signature_name": "serving_default", "instances": reshaped_image.tolist()})
headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/obj_det:predict', data=data, headers=headers)
predictions = json.loads(json_response.text)
print(predictions)
