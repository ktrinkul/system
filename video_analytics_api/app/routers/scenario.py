from fastapi import APIRouter
from video_analytics_api.app.routers.state_management import router as state_management_router

router = APIRouter()

# Existing scenario routes

# Include the state management router
router.include_router(state_management_router, prefix="/scenario", tags=["state management"])
