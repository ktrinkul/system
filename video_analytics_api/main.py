def main():
    """Entry point for the video analytics API. Handles routing and startup procedures."""
    try:
        # Initialize the application
        app = create_app()
        # Load configurations and set up database
        configure_db(app)
        # Start the application
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        # Log the error for diagnostics
        print(f'Error while starting the API: {e}')
        raise
