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
        species_df = data_dict['results']
        species_df = pd.DataFrame(species_df)
        fd=fd.append(species_df)
    return fd.reset_index(drop=True)

#creation du dataframe correspondant a partir du nom de l'entite (vehicles,people...)
def dfswapi(entite):
    link=lien(entite)
    df=dataframe(link,page_number(entity_number(dico((link)))))
    return df

dfswapi(input('quel entite voulez-vous ?'))