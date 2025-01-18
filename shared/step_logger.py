import logging
logger = logging.getLogger(__name__)

class StepLogger:
    """Step logger class."""
    def __init__(self, step_name: str):
        """Initialize StepLogger class."""
        self.step_name = step_name

    def __enter__(self):
        """Log step start."""
        logger.info(f"\n============================ {self.step_name} step started. ============================")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Log step finish."""
        logger.info(f"\n============================ {self.step_name} step finished. ============================")
