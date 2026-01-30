def run_application() -> None:
    """Starts the video analytics application."""
    try:
        # Initialize the application components
        initialize_components()
        # Start the main application loop
        main_loop()
    except Exception as e:
        # Log the error and safely shut down the application
        log_error(f'Application crashed due to: {e}')
        shutdown_application()  # Graceful shutdown method

    if __name__ == '__main__':
        run_application()