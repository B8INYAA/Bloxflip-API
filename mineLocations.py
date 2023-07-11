import requests

AUTH = "INSERT_BLOXFLIP_AUTH_HERE"
SIZE = 6

r = requests.post("https://api.bloxflip-predictors.xyz/v1/mines/GetHistory/mineLocations", json={"auth": AUTH, "size": SIZE}).json

DATA = r["mineLocations"]