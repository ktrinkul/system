def main():
    """Main entry point of the video analytics API. Initializes the app and starts the server."""
    try:
        app = FastAPI()
        app.include_router(scenario_router)
        app.include_router(outbox_router)
        # Additional setup if needed

        # Running the application
        uvicorn.run(app, host='0.0.0.0', port=8000)
    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')
        raise

if __name__ == '__main__':
    main()