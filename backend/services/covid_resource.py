from core.mongodb import AsyncIOMotorClient
from typing import List
import logging as logger
from datetime import datetime, timedelta
from core.config import database_name, covidIn_collection_name
from models import ResourceIn, ResourceOut


async def create_covid_resource(payload, conn: AsyncIOMotorClient):
    try:
        row = await conn[database_name][covidIn_collection_name].insert_one(payload.dict())
        statusCode = "200"
        message = "Saved Successfully"
    except Exception as e:
        statusCode = "504"
        message = "Internal Server Error"

    return {"statusCode": statusCode, "message": message}

async def get_covid_resources(conn: AsyncIOMotorClient):
    try:
        result = {}
        counter = 1
        async for lead in conn[database_name][covidIn_collection_name].find():
            lead.pop('_id')
            result[counter] = lead
            counter += 1
        statusCode = "200"
        message = result
    except Exception as e:
        statusCode = "504"
        message = "Internal Server Error"

    return {"statusCode": statusCode, "message": message}
async def get_covid_resource_by(location, resource_type, conn: AsyncIOMotorClient):
    try:
        result = {}
        counter = 1
        async for lead in conn[database_name][covidIn_collection_name].find({"location":location, "resource":resource_type}):
            lead.pop('_id')
            result[counter] = lead
            counter += 1
        statusCode = "200"
        message = result
    except Exception as e:
        statusCode = "504"
        message = "Internal Server Error"

    return {"statusCode": statusCode, "message": message}