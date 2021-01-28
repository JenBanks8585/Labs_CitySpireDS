import os
import requests

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import sqlalchemy
from pydantic import BaseModel, SecretStr

from app import config

router = APIRouter()

headers = {'x-rapidapi-key': os.getenv('api_key'),
           'x-rapidapi-host': os.getenv('host') }

class RentalList(BaseModel):
    api_key: SecretStr = config.settings.api_key
    city: str = "New York"
    state: str = "NY"
    prop_type: str = "condo"
    limit: int = 5


@router.get('/for_rent_list_base')
async def for_rent_list_base(rentallist: RentalList):

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
    querystring = {"city": rentallist.city,
                 "state_code": rentallist.state,
                 "limit": rentallist.limit,
                 "offset": "0",                 
                 "sort":"relevance",
                 "prop_type": rentallist.prop_type}

    response_for_rent = requests.request("GET", url, params = querystring, headers = headers,)
    return response_for_rent.json()