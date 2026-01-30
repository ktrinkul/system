import logging
from fastapi import FastAPI
import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.exception_handler(Exception)
async def handle_exception(request, exc):
    logger.error(f"Unexpected error: {exc}")
    return JSONResponse(status_code=500, content={'message': 'Internal server error'})

if __name__ == '__main__':
    logger.info('Starting API server...')
    uvicorn.run(app, host='0.0.0.0', port=8000)