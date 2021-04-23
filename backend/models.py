from datetime import datetime, timezone
from pydantic import BaseConfig, BaseModel, Field
from typing import Dict, Optional, List

# # Base Model
class RWModel(BaseModel):
    class Config(BaseConfig):
        allow_population_by_alias = True
        json_encoders = {
            datetime: lambda dt: dt.replace(tzinfo=timezone.utc)
            .isoformat()
            .replace("+00:00", "Z")
        }

class ResourceIn(RWModel):
    lead: str
    quanitiy: str
    details: str
    contact_name: str
    contact_phone: str
    source_name: str
    source_phone: str
    verified: str
    location: str
    address: str
    source: str


class ResourceOut(RWModel):
    resource: str
    quanitiy: str
    details: str
    contact_name: str
    contact_phone: str
    source_name: str
    source_phone: str
    verified: str
    location: str
    address: str
    source: str