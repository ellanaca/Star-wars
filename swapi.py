import requests
import pandas as pd
import warnings
import numpy as np
from math import ceil
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


def name_url_people():   
    
    #Appel API
    request=requests.get(url)

    #Create Dataframe of result
    json_list = request.json()["results"]
    json_list_df = pd.DataFrame(json_list)

    #Iterate for each line
    for line in range(10) :
        json_list_series_resident = json_list_df["residents"][line]

        #create empty list
        people_list = []


        #iterate for each URL in cell
        for data in json_list_series_resident:

            response = requests.get(data)
            get =people_list.append(response.json()["name"])


            json_list_df["residents"][line] = people_list
            
    return json_list_df
     

