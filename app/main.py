
from fastapi import FastAPI, Depends
import requests
import uvicorn
import json
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel, SecretStr

from app import realty, realtybasemodel

description = """
To use these interactive docs:
- Click on an endpoint below
- Click the **Try it out** button
- Edit the Request body or any parameters
- Click the **Execute** button
- Scroll down to see the Server response Code & Details
"""

app = FastAPI(
    title = "Jen's Realty API",
    description = description,
    docs_url = '/')
 
  
app.include_router(realty.router, tags=['Realty'])
app.include_router(realtybasemodel.router, tags=['Realty Using BaseModel'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
