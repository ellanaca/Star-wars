import requests
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#Call the API
def reponse(entite):
    url = f"https://swapi.dev/api/{entite}"
    response = requests.get(url)
    return response
reponse("planets")
