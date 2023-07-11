# [Bloxflip API](https://api.bloxflip-predictors.xyz/)
A bloxflip api alternative created by Blix.

## Predicting 

Import requests
```python
import requests
```

Define the Bloxflip AUTH you want to predict with

```python
AUTH = "INSERT_BLOXFLIP_AUTH_HERE"
```

Send a request to the API

```python
r = requests.post("https://api.bloxflip-predictors.xyz/v1/mines/predict", json={"auth": AUTH})
```




