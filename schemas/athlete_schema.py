def athleteEntity(item) -> dict:
    return{
        "_id": str(item["_id"]),
        "name_athlete" : str(item["name_athlete"]),
        "lastname_athlete": str(item["lastname_athlete"]),
        "age": int(item["age"]),
        "description_athlete": str(item["description_athlete"])
    }

def completeAthleteEntity(item) -> dict:
     return{
        "_id": str(item["_id"]),
        "name_athlete" : str(item["name_athlete"]),
        "lastname_athlete": str(item["lastname_athlete"]),
        "age": int(item["age"]),
        "description_athlete": str(item["description_athlete"]),
        "exercises": str(item["exercises"])
    }


def athletesEntity(cursor) -> list:
    data = []
    for item in cursor:
        data.append(athleteEntity(item))
    return data


def completeAthletesEntity(cursor)-> list:
    data = []
    for item in cursor:
        data.append(completeAthleteEntity(item))
    return data






















