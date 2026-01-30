def main():
    """Main entry point of the video analytics orchestrator. Initializes the orchestrator and starts processing."""
    try:
        orchestrator = Orchestrator()
        orchestrator.start()
    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')
        raise

if __name__ == '__main__':
    main()