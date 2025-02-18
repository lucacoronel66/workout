from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from models.workout_model import WorkoutExcercise
from schemas.workout_schema import workoutEntity, workoutsEntity
from config.database import conn
from bson import ObjectId



workout = APIRouter(prefix="/workout", tags=["WORKOUT"])


@workout.get("/")
def get_workout():
    try:
        workout = conn.local.workout.find()
        complete_workout = workoutsEntity(workout)

        if complete_workout:
            return JSONResponse(content= complete_workout, status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content="No se encontró data",
             status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)}, 
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@workout.get("/{id}")
def get_workout_id(id : str):
    try:
        data_workout = workoutEntity(conn.local.workout.find_one({"_id": ObjectId(id)}))

        if data_workout:
            return JSONResponse(content=data_workout, status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content= "NO SE ENCONTRÓ DATA", status_code= status.HTTP_204_NO_CONTENT)
        
    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@workout.post("/")
def create_workout(workout: WorkoutExcercise):
    try:
        new_workout = workout.dict()
        result = conn.local.workout.insert_one(new_workout)
        new_workout["_id"] = str(result.inserted_id)
        return JSONResponse(content="WORKOUT CREADO", status_code= status.HTTP_200_OK)                
    
    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@workout.put("/{id}")
def update_workout(id: str):
    try:
        data_workout= conn.local.workout.find_one({"_id": ObjectId(id)})
        if data_workout:
            conn.local.workout.update_one(
                {"_id": ObjectId(id)},

                {"$set": dict(workout)}
                 )
            
            return JSONResponse(content="ACTUALIZADO CORRECTAMENTE", status_code=status.HTTP_200_OK)
        
        else:
            return JSONResponse(content="NOS SE ENCONTRO UN WORKOUT CON ESE ID", status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@workout.delete("/{id}")
def delete_workout(id: str):
    try:
        workout_result = conn.local.workout.delete_one({"_id": ObjectId(id)})
        
        if workout_result:
            return JSONResponse(content="BORRADO EXITOSAMENTE", status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content="NO SE ENCONTRÓ UN WORKOUT CON ESE ID")

    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )






