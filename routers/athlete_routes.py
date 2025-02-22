from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from models.athlete_model import Athlete, completeAthlete
from schemas.athlete_schema import athleteEntity, athletesEntity, completeAthletesEntity, completeAthleteEntity
from config.database import conn
from bson import ObjectId



athlete = APIRouter(prefix="/athlete", tags=["ATLETA"])
complete_athlete = APIRouter(prefix="/complete_athlete", tags= ["ATLETA COMPLETO"])

@athlete.post("/")
def create_athlete(athlete: Athlete):
    try:
        new_athlete = athlete.dict()
        
        result = conn.local.athlete.insert_one(new_athlete)
        new_athlete["_id"] = str(result.inserted_id)

        return JSONResponse(content="Atleta creado", status_code=status.HTTP_201_CREATED)
    
    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@athlete.get("/")
def get_athlete():
    try:
        athlete_complete = athletesEntity(conn.local.athlete.find())

        if athlete_complete:
            return JSONResponse(content=athlete_complete, status_code=status.HTTP_200_OK)
        
        else:
            return JSONResponse(content="No se encontró ningun atleta", status_code= status.HTTP_204_NO_CONTENT)
                
    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        ),

@athlete.get("/{id}")
def get_athlete_id(id: str):
    try:
        data_athlete = conn.local.athlete.find_one({"_id": ObjectId(id)})
        complete_data = athleteEntity(data_athlete)
        if complete_data:

            return JSONResponse(content = complete_data, status_code= status.HTTP_200_OK)
        else: 
            return JSONResponse(content="No se encontró el atleta con ese ID")
        
    except Exception as e: 
        print(f"Error general: {e}")

        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    
@athlete.delete("/{id}")
def delete_athlete(id: str):
    try:
        athlete_result = conn.local.athlete.delete_one({"_id": ObjectId(id)})

        if athlete_result:
            return JSONResponse(content="ATLETA ELIMINADO", status_code= status.HTTP_200_OK)
        else: 
            return JSONResponse(content="No se encontró el atleta con ese ID")
    
    except Exception as e: 
        return JSONResponse(
                content={"error": "Error en el servidor", "details": str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    
@athlete.put("/{id}")
def updateAthlete(id: str, athlete: Athlete):
    
    try: 
        athlete_data = conn.local.athlete.find_one({"_id": ObjectId(id)})
        if athlete_data:
            conn.local.exercise.update_one({"_id": ObjectId(id)}, {"$set": dict(athlete)})

            return JSONResponse(content= "ACTUALIZADO", status_code=status.HTTP_200_OK)
        

    except Exception as e: 
        return JSONResponse(
                content={"error": "Error en el servidor", "details": str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


@complete_athlete.post("/")
def createCompleteAthlete(complete_athlete: completeAthlete):

    try:
        new_complete_athlete = complete_athlete.dict()
        result = conn.local.complete_athlete.insert_one(new_complete_athlete)
        new_complete_athlete["_id"] = str(result.inserted_id)
        return JSONResponse(content="CREADO", status_code=status.HTTP_201_CREATED)
    
    except Exception as e: 
        return JSONResponse(
                content={"error": "Error en el servidor", "details": str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

@complete_athlete.get("/")
def getCompleteAthlete():

    try:
        complete_athlete = completeAthletesEntity(conn.local.complete_athlete.find())
        if complete_athlete:
            return JSONResponse(content= complete_athlete, status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content= "NO SE ENCONTRÓ CONTENIDO", status_code=status.HTTP_200_OK)
    except Exception as e: 
        return JSONResponse(
                content={"error": "Error en el servidor", "details": str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
            

@complete_athlete.get("/{id}")
def getCompleteAthleteID(id: str):
    try:
        complete_athlete = conn.local.complete_athlete.find_one({"_id": ObjectId(id)})
        complete_data = completeAthleteEntity(complete_athlete)

        if complete_data:
            return JSONResponse(content=complete_data, status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content="NO SE ENCONTRÓ ESE ID", status_code=status.HTTP_200_OK)
        
    except Exception as e: 
        return JSONResponse(
                content={"error": "Error en el servidor", "details": str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

@complete_athlete.delete("/{id}")
def deleteCompleteAthlete(id: str):
    try:
        result = conn.local.complete_athlete.delete_one({"_id": ObjectId(id)})
        if result:
            return JSONResponse(content="ELIMINADO", status_code=status.HTTP_201_CREATED)
        else:
            return JSONResponse(content="ID NO ENCONTRADO")
        
    except Exception as e:
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@complete_athlete.put("/{id}")
def updateCompleteAthlete(id: str, complete_athlete: completeAthlete):
    try:
        complete_athlete_data = conn.local.complete_athlete.find_one({"_id": ObjectId(id)})

        if complete_athlete_data:
            update_complete_athlete_data = complete_athlete.model_dump()

            conn.local.complete_athlete.update_one(
                {"_id": ObjectId(id)},

                {"$set": update_complete_athlete_data}
            )
            return JSONResponse(content="ACTUALIZADO", status_code= status.HTTP_200_OK)
        else:
            return JSONResponse(content="NO SE ENCONTRÓ ESE ID", status_code=status.HTTP_200_OK)
    
    except Exception as e:
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )










