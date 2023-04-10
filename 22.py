import requests
from requests.exceptions import InvalidURL

try:
    response = requests.get("httpssdws:ddsfd ds")
except InvalidURL:
    print("invalid url was given")