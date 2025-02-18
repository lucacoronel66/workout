from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from models.athlete_model import Athlete
from schemas.athlete_schema import athleteEntity, athletesEntity
from config.database import conn
from bson import ObjectId



athlete = APIRouter(prefix="/athlete", tags=["ATHLETE"])

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
def update_athlete(id: str, athlete: Athlete):
    
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





 















