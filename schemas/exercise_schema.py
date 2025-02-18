from config.database import conn
from .workout_schema import workoutEntity

def completeExerciseEntity(item) -> dict:

    return {
        "_id": str(item["_id"]),
        "id_athlete": str(item["id_athlete"]),
        "name": str(item["name"]),
        "description": str(item["description"]),
        "muscle_group": str(item["muscle_group"]),
        "workout": item.get("workout", {"sets": 0, "reps": 0, "weight": 0})
    }

def completeExercicesEntity(cursor) -> list:
    data = []
    for item in cursor:
        data.append(completeExerciseEntity(item))
    return data

def exerciseEntity(item) -> dict:
    return{
        "_id": str(item["_id"]),
        "id_athlete": str(item["id_athlete"]),
        "name": str(item["name"]),
        "description": str(item["description"]),
        "muscle_group": str(item["muscle_group"])
    }

def exercisesEntity(cursor) -> list:
    data = []
    for item in cursor:
        data.append(exerciseEntity(item))
    return data




