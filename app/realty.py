"""Realty Info"""

import os
import requests

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import sqlalchemy
from pydantic import BaseModel, SecretStr

from app import config, walk_score

load_dotenv()

router = APIRouter()

headers = {'x-rapidapi-key': os.getenv('api_key'),
           'x-rapidapi-host': os.getenv('host') }


@router.get('/streamlined_rent_list')
async def streamlined_rent_list(api_key = config.settings.api_key, 
             city: str = "New York City", 
             state: str= "NY", 
             prop_type: str = "condo", 
             limit: int = 4):

    """
    Parameters:
        api_key
        city: str 
        state: str
        prop_type: str ('condo', 'single_family', 'multi_family')
        limit: int number of results to populate

    Returns:
        information about properties for rent
    """
    url = os.getenv('url_list_for_rent')
    querystring = {"city": city,
                 "state_code": state,
                 "limit": limit,
                 "offset": "0",                 
                 "sort":"relevance",
                 "prop_type": prop_type}

    response_for_rent = requests.request("GET", url, params = querystring, headers = headers,)
    response = response_for_rent.json()['properties']

    rental_list = []
    for i in range(len(response)):
      line = response[i]['address']['line']
      city = response[i]['address']['city']
      state = response[i]['address']['state']
      lat = response[i]['address']['lat']
      lon = response[i]['address']['lon']
      photos = response[i]['photos']
      address = line +" "+  city + " "+ state
      walk_score = get_walk_score(addre, lat, lon)
      element = {'address': address, 'lat': lat, 'lon': lon, 'city':city, 'state':state, 'photos': photos,  'walk_score': walk_score}
      rental_list.append(element)

    return rental_list
  
@router.get('/for_rent_list')
async def for_rent_list(api_key = config.settings.api_key, 
             city: str = "New York City", 
             state: str= "NY", 
             prop_type: str = "condo", 
             limit: int = 4):

    """
    Parameters:
        api_key
        city: str 
        state: str
        prop_type: str ('condo', 'single_family', 'multi_family')
        limit: int number of results to populate

    Returns:
        information about properties for rent
    """
    url = os.getenv('url_list_for_rent')
    querystring = {"city": city,
                 "state_code": state,
                 "limit": limit,
                 "offset": "0",                 
                 "sort":"relevance",
                 "prop_type": prop_type}

    response_for_rent = requests.request("GET", url, params = querystring, headers = headers,)
    return response_for_rent.json()['properties']


@router.get('/for_rent_list/{property_id}')
async def property_detail(property_id: str = "O3599084026"):
    """
    Parameters: 
        property_id
    Returns:
        detailed information about the property
    """
    url = os.getenv('url_property_detail')
    querystring = {"property_id":property_id}
    
    response_prop_detail = requests.request("GET", url, headers=headers, params=querystring)
    return response_prop_detail.json()['properties']


@router.get('/for_sale_list')
async def for_sale_list(api_key = config.settings.api_key, 
             city = "New York City", 
             state= "NY",             
             limit = ):

    
    url = os.getenv('url_list_for_sale')
    querystring = {"city": city ,"limit": limit,"offset":"0","state_code": state,"sort":"relevance"}

    response_for_sale = requests.request("GET", url, headers=headers, params=querystring)
    return response_for_sale.json()['properties']



