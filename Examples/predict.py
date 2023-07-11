import requests

AUTH = "INSERT_BLOXFLIP_AUTH_HERE"

r = requests.post("https://api.bloxflip-predictors.xyz/v1/mines/predict", json={"auth": AUTH}).json

PREDICTION = r["prediction"]