def athleteEntity(item) -> dict:
    return{
        "_id": str(item["_id"]),
        "name_athlete" : str(item["name_athlete"]),
        "lastname_athlete": str(item["lastname_athlete"]),
        "age": int(item["age"]),
        "description_athlete": str(item["description_athlete"])
    }

def athletesEntity(cursor) -> list:
    data = []
    for item in cursor:
        data.append(athleteEntity(item))
    return data


def completeAthleteEntity(item) -> dict:
     return{
         "_id": str(item["_id"]),
        "name_athlete" : str(item["name_athlete"]),
        "lastname_athlete": str(item["lastname_athlete"]),
        "age": int(item["age"]),
        "description_athlete": item.get("description_athlete"),
        "exercises": item.get("exercises")
    }

def completeAthletesEntity(cursor)-> list:
    data = []
    for item in cursor:
        data.append(completeAthleteEntity(item))
    return data


def descriptionAthleteEntity(item) -> dict:
    return{
        "gender": str(item["gender"]),
        "athlete_weight": str(item["athlete_weight"]),
        "goal_athlete": str("goal_athlete"),
        "athlete_status": str("athlete_status")
    }


def descriptionsAthleteEntity(cursor) -> list:
    data = []
    for item in cursor:
        data.append(descriptionAthleteEntity(item))
    return data















