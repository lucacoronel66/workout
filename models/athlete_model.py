from pydantic import BaseModel
from typing import Optional

class Athlete(BaseModel):
    _id: Optional[str]
    name_athlete: str
    lastname_athlete: str
    age: int
    description_athlete: str



    

