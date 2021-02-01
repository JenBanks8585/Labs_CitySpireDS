from walkscore import WalkScoreAPI
from pydantic import BaseModel
from fastapi import APIRouter
from app import config
import os
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()

def what_message(score):
    if 90 <= score <= 100:
        return "daily errands do not require a car"
    elif 70 <= score <= 89:
        return "most errands can be accomplished on foot"
    elif 50 <= score <= 69:
        return "some errands can be accomplished on foot"
    elif 25 <= score <= 49:
        return "most errands require a car"
    else:
        return " almost all errands require a car"


@router.get('/walk_score')
async def get_walk_score(address: str = "7 New Port Beach, Louisiana",
    lat: float = 39.5984,
    lon: float = -74.2151
    ):

    walk_api = WalkScoreAPI(api_key= os.getenv('walk_api'))

    result = walk_api.get_score(longitude = lon, 
            latitude = lat,
            address = address)
    
    message = what_message(result.walk_score)

    return {"walk_socore": result.walk_score, "walk_message":message}



