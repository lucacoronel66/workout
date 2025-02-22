from fastapi import FastAPI
from routers.exercise_routes import exercise, complete_exercise
from routers.workout_routes import workout
from routers.athlete_routes import athlete, complete_athlete
app = FastAPI()


app.include_router(complete_athlete)
app.include_router(complete_exercise)
app.include_router(athlete)
