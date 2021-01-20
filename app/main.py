
from fastapi import FastAPI, Depends
import requests
import uvicorn
import json
import pandas as pd
import os
from pydantic import BaseModel, SecretStr
from dotenv import load_dotenv
import config
from app import realty

load_dotenv()

description = """
To use these interactive docs:
- Click on an endpoint below
- Click the **Try it out** button
- Edit the Request body or any parameters
- Click the **Execute** button
- Scroll down to see the Server response Code & Details
"""

app = FastAPI(debug = True, 
              title = "Realty API",
             description = description,
             docs_url = '/')
 
  
app.include_router(realty.router, tags=['Realty'])
app.include_router(pollution.router, tags=['Pollution'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
