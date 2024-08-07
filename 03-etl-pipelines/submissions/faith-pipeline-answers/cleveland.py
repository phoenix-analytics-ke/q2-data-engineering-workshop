
def assignment_clevelandart():
    """
    From the API endpoint in the comment, extract data of creators who are english in nationationality,
    birth year after 1960 and death year before 2020
    Your function should return data in JSON format
    """
    url
#https://openaccess-api.clevelandart.org/api/creators/?nationality=french&birth_year_before=1940
# https://openaccess-api.clevelandart.org/api/creators/

import requests
import pprint
import pandas as pd

#ingesting the data from the URL

#modular function
def get_creators ():
    Base_url='https://openaccess-api.clevelandart.org/api/creators/'
    params ={
        'birth_year_before': 1960,
        'death_year_after': 2020,
        'nationality': 'French'
    }
    creators=requests.get(Base_url, params=params)
    data = creators.json()

creator_data=get_creators()
