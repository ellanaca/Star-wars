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

#get the number of entities
def entity_number(data_dict) :
    a=data_dict['count']
    return a