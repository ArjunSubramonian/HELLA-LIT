# USAGE
# python simple_request.py

import sys
sys.path.insert(0, 'src')
from utils import save_img

# import the necessary packages
import requests
import scipy.misc, numpy as np, os, sys
import base64
import json

# initialize the TF REST API endpoint URL along with the input
# image path
TF_REST_API_URL = "http://127.0.0.1:5000/predict"
IMAGE_PATH = "test.jpeg"
MODEL_PATH = "models/rain_princess.ckpt"
OUT_PATH = "out.jpg"

# construct the payload for the request
payload = {"image": IMAGE_PATH, "model": MODEL_PATH}
payload = json.dumps(payload)
payload = json.loads(payload)

# submit the request
r = requests.post(TF_REST_API_URL, data=payload).json()
print(r)

# ensure the request was sucessful
if r["success"]:
    with open(OUT_PATH, "wb") as out_file:
        out_file.write(base64.b64decode(r["prediction"].encode('ascii')))
# otherwise, the request failed
else:
    print("Request failed")