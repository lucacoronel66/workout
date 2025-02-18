from pydantic import BaseModel
from typing import Optional, List

class WorkoutExcercise(BaseModel):
        
        sets: int
        reps: int
        weight: Optional[int]




        