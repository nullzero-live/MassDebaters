import logging

class LoggerUtility:
    def __init__(self, name, log_level=logging.INFO, log_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"):
        # Initialize the logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        # Create console handler and set its log level
        ch = logging.StreamHandler()
        ch.setLevel(log_level)

        # Create formatter and add it to the handler
        formatter = logging.Formatter(log_format)
        ch.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(ch)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)

    def debug(self, message):
        self.logger.debug(message)

    def critical(self, message):
        self.logger.critical(message)

# Usage
log_util = LoggerUtility(name="MyApp")
log_util.info("This is an info message")
log_util.error("This is an error message")

In the above code:

    The LoggerUtility class initializ
