# backend/app/core/logger.py

import logging
import sys


def get_logger(name: str = "firesight") -> logging.Logger:
    """
    Create and return a configured logger instance.
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers when using --reload
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False

    return logger


# Shared application logger
logger = get_logger()