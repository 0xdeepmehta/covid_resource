from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from core.mongodb_utils import startup_event, shutdown_event
from models import ResourceIn, ResourceOut
from core.mongodb import AsyncIOMotorClient, get_database
from services.covid_resource import create_covid_resource, get_covid_resource_by, get_covid_resources
app = FastAPI()

origins = [
    # "http://localhost",
    # "http://127.0.0.1:5501",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # put here the producation frontend url
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)


@app.post("/lead", tags=["COVID LEADS"])
async def lead_save(payload: ResourceIn, db: AsyncIOMotorClient = Depends(get_database)):
    # payload = payload.dict()
    # print(payload)
    s_response = await create_covid_resource(payload, db)
    return s_response

@app.get("/leads", tags=["COVID LEADS"])
async def lead_get(db: AsyncIOMotorClient = Depends(get_database)):
    s_response = await get_covid_resources(db)
    return s_response

@app.get("/lead_by", tags=["COVID LEADS"])
async def lead_get(location:str, resource_type:str, db: AsyncIOMotorClient = Depends(get_database)):
    s_response = await get_covid_resource_by(location, resource_type, db)
    return s_response