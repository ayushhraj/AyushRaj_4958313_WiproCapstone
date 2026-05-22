import logging
import os


class LogGenerator:

    @staticmethod
    def loggen():

        # Create logs folder if not present
        if not os.path.exists("logs"):
            os.makedirs("logs")

        logger = logging.getLogger("BestBuy")

        logger.setLevel(logging.INFO)

        # Prevent duplicate handlers
        if not logger.handlers:

            file_handler = logging.FileHandler(
                "logs/automation.log"
            )

            formatter = logging.Formatter(
                "%(asctime)s : %(levelname)s : %(message)s"
            )

            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger