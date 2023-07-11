## Predicting Mines

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
r = requests.post("https://api.bloxflip-predictors.xyz/v1/mines/predict", json={"auth": AUTH}).json
```

Get your prediction

```python
PREDICTION = r["prediction"]
```

## Getting Mines History

Import requests
```python
import requests
```

Define the Bloxflip AUTH you want to get the history of and the size of the history you want

```python
AUTH = "INSERT_BLOXFLIP_AUTH_HERE"
SIZE = 6
```

Send a request to the API

```python
r = requests.post("https://api.bloxflip-predictors.xyz/v1/mines/GetHistory", json={"auth": AUTH, "size": SIZE}).json
```

Get your Data

```python
DATA = r["data"]
```

## Getting Mines mineLocations History

Import requests
```python
import requests
```

Define the Bloxflip AUTH you want to get the history of and the size of the history you want

```python
AUTH = "INSERT_BLOXFLIP_AUTH_HERE"
SIZE = 6
```

Send a request to the API

```python
r = requests.post("https://api.bloxflip-predictors.xyz/v1/mines/GetHistory/mineLocations", json={"auth": AUTH, "size": SIZE}).json
```

Get your Data

```python
DATA = r["mineLocations"]
```

## Getting Mines uncoveredLocations History

Import requests
```python
import requests
```

Define the Bloxflip AUTH you want to get the history of and the size of the history you want

```python
AUTH = "INSERT_BLOXFLIP_AUTH_HERE"
SIZE = 6
```

Send a request to the API

```python
r = requests.post("https://api.bloxflip-predictors.xyz/v1/mines/GetHistory/uncoveredLocations", json={"auth": AUTH, "size": SIZE}).json
```

Get your Data

```python
DATA = r["uncoveredLocations"]
```



