# Logging Module

import logging

def setup_logger(name):
    """Setup a logger with the given name."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
