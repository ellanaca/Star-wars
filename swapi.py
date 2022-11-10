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

def page_number(number) :
    page=ceil(number/10)
    return page

#get the number of entities
def entity_number(data_dict) :
    a=data_dict['count']
    return a

def bb(link,page):
fd=pd.DataFrame()
for x in range(1,page+1) :
    request=requests.get(link+str(x))
    data_dict = request.json()
    species_df = data_dict['results']
    species_df = pd.DataFrame(species_df)
    fd=fd.append(species_df)
return fd