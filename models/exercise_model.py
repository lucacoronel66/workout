from pydantic import BaseModel
from typing import Literal, Optional
from .workout_model import WorkoutExcercise



class Exercise(BaseModel):
    _id: str
    id_athlete: str
    name : str
    description : str
    muscle_group: str

class CompleteExercise(Exercise):
    workout: WorkoutExcercise

    



