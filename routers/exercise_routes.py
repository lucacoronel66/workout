from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from models.exercise_model import Exercise, CompleteExercise
from schemas.exercise_schema import exerciseEntity, exercisesEntity, completeExerciseEntity, completeExercicesEntity
from config.database import conn
from bson import ObjectId

exercise = APIRouter(prefix="/exercise", tags=["EXERCISE"])

complete_exercise = APIRouter(prefix="/complete_exercise", tags=["COMPLETE EXERCISE"])


@exercise.get("/{id}")
def get_exercise_id(id: str):
    try:
        data_exercise = exerciseEntity(conn.local.exercise.find_one({"_id": ObjectId(id)}))

        if data_exercise:
            return JSONResponse(content=data_exercise, status_code= status.HTTP_200_OK)
        else:
            return JSONResponse(content="No se encontró data", status_code= status.HTTP_200_OK)

    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    
@exercise.get("/")
async def get_exercise():
    try:
        exercise = conn.local.exercise.find()
        complete_exercise = exercisesEntity(exercise)
        if complete_exercise:
            return JSONResponse(content= complete_exercise, status_code= status.HTTP_200_OK)
        else:
            return JSONResponse(content="No se encontraron datos", status_code=status.HTTP_200_OK)
        
    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    
    
@exercise.post("/", status_code=status.HTTP_201_CREATED)
def create_exercise(exercise: Exercise):  
    try:
        new_exercise = exercise.dict()

        result = conn.local.exercise.insert_one(new_exercise)

        new_exercise["_id"] = str(result.inserted_id)

        return JSONResponse(content="EJERCICIO CREADO", status_code=status.HTTP_201_CREATED)
    
    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@exercise.put("/{id}")
def update_exercise(id: str, exercise: Exercise):
    try:
        data_exercise = conn.local.exercise.find_one({"_id": ObjectId(id)})

        if data_exercise:

            conn.local.exercise.update_one(
                {"_id": ObjectId(id)},

                {"$set": dict(exercise)}
                 )
            return JSONResponse(content="ACTUALIZADO CORRECTAMENTE", status_code= status.HTTP_200_OK)
        
        else:
            return JSONResponse(content="NO SE ENCONTRÓ ESE ID", status_code= status.HTTP_204_NO_CONTENT)

    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    

@exercise.delete("/{id}")
def delete_exercise(id: str):
    try:
        exercise_result = conn.complete_exercise.delete_one({"_id": ObjectId(id)})
        if exercise_result: 
            return JSONResponse(content="EJERCICIO ELIMINADO", status_code=status.HTTP_200_OK) 
        else: 
            return JSONResponse(content="No se encontraron datos", status_code=status.HTTP_204_NO_CONTENT)
    
    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@complete_exercise.post("/")
def create_complete_exercise(complete_exercise: CompleteExercise):
    
    try:
        complete_exercise = complete_exercise.dict()
        result = conn.local.complete_exercise.insert_one(complete_exercise)
        complete_exercise["_id"] = str(result.inserted_id)
        
        return JSONResponse(content="Creado", status_code=status.HTTP_201_CREATED)
        
    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@complete_exercise.get("/")
def get_complete_exercise():
    try:
        data =  conn.local.complete_exercise.find()
        complete_exercices = completeExercicesEntity(data)
        if complete_exercices:
            return JSONResponse(content=complete_exercices, status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content="No se encontraron los datos", status_code=status.HTTP_204_NO_CONTENT)
        
    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@complete_exercise.get("/{id}")
def get_complete_exercise_id(id_athete):
    try:
        exercise = conn.local.complete_exercise.find_one({"_id": ObjectId(id_athete)})
        complete_exercise = completeExerciseEntity(exercise)
        
        if complete_exercise:
            return JSONResponse(
                content= complete_exercise, status_code=status.HTTP_200_OK
            )
        else:
            return JSONResponse(content="No se encontró ese ID", status_code=status.HTTP_204_NO_CONTENT)        

    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

@complete_exercise.delete("/{id}")
def delete_complete_exercise(id : str):
    try:
        complete_exercise_result = conn.local.complete_exercise.delete_one({"_id": ObjectId(id)})
        if complete_exercise_result: 
            return JSONResponse(content="Eliminado", 
                                status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content="No se encontró el ID", 
                                status_code= status.HTTP_204_NO_CONTENT)
        
    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    
@complete_exercise.put("/{id}")
def update_complete_exercise(id:str, complete_exercise: CompleteExercise):
    try:
        data_exercise = conn.local.complete_exercise.find_one({"_id": ObjectId(id)})

        if data_exercise:
            update_data = complete_exercise.model_dump()
            conn.local.complete_exercise.update_one(
                {"_id": ObjectId(id)},

                {"$set": update_data}
                 )
            return JSONResponse(content="ACTUALIZADO", status_code= status.HTTP_200_OK)
        
        else:
            return JSONResponse(content="NO SE ENCONTRÓ ESE ID", status_code= status.HTTP_204_NO_CONTENT)
    except Exception as e:
        print(f"Error general: {e}")
        return JSONResponse(
            content={"error": "Error en el servidor", "details": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
        
















