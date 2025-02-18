def workoutEntity(item) -> dict:
    return{
        "sets": int(item["sets"]),
        "reps": int(item["reps"]),
        "weight": int(item["weight"]) 
    }


def workoutsEntity(cursor) -> list:
    data = []

    for item in cursor:
        data.append(workoutEntity(item))
    
    return data

