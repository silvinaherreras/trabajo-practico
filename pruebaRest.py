import requests
from requests.auth import HTTPDigestAuth
import json

def pruebaRst():
    api_url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(api_url)
    salida=response.json()
    print (salida)

pruebaRst()

