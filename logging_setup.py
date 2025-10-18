import logging
import os

def logging_setup(name, log_file='server.log', level=logging.DEBUG):
    # Ensure folder exists
    os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Only add handlers once
    if not logger.handlers:
        # File handler
        file_handler = logging.FileHandler(log_file)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # Optional: console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger

# Test
logger = logging_setup("db_helper", "backend/server.log")
logger.info("Logger is working!")
