from fastapi import FastAPI
from video_analytics_api.app.routers import new_scenario

app = FastAPI()

app.include_router(new_scenario.router, prefix='/api')  # Adding new router

# Existing setup and routes remain here
