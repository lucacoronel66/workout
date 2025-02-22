from pydantic import BaseModel
from typing import Optional
from .exercise_model import CompleteExercise

class DescriptionAthlete(BaseModel):
    _id: Optional[str]
    gender: str
    athlete_weight: int
    goal_athlete : str
    athlete_status: str

class Athlete(BaseModel):
    _id: Optional[str]
    name_athlete: str
    lastname_athlete: str
    age: int
    
class completeAthlete(Athlete):
    description_athlete: DescriptionAthlete
    exercises: CompleteExercise
    

