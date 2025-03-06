
from typing import List
from pydantic import BaseModel


class Properties(BaseModel):
    x: float
    y: float

class FeatureSearch(BaseModel):
    properties: Properties