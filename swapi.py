import requests
import pandas as pd
import warnings
import numpy as np
from math import ceil
warnings.filterwarnings('ignore')

#Generation du lien
def lien(entite) :
    debut ="https://swapi.dev/api/"
    link=debut+entite+'/'
    return link

#Generation du dictionnaire
def dico(link) :
    response = requests.get(link)
    data_dict = response.json()
    return data_dict

#extraction du nombre d'entite
def entity_number(data_dict) :
    a=data_dict['count']
    return a

#calcul du nombre de pages
def page_number(number) :
    page=ceil(number/10)
    return page

#creation de dataframe
def dataframe(link,page):
    fd=pd.DataFrame()
    for x in range(1,page+1) :
        request=requests.get(link+'/?page='+str(x))
        data_dict = request.json()
        df = data_dict['results']
        df = pd.DataFrame(df)
        fd=fd.append(df)
    return fd.reset_index(drop=True)


def name_url_people(entite):   
    
    #Appel API
    request=requests.get(lien(entite))

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
     

    

#creation du dataframe correspondant a partir du nom de l'entite (vehicles,people...)
def dfswapi(entite):
    link=lien(entite)
    df=dataframe(link,page_number(entity_number(dico((link)))))
    return df

dfswapi(input('quel entite voulez-vous ?'))
