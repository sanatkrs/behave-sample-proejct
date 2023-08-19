import logging
from pathlib import Path


class LogGen:
    @staticmethod
    def loggen():
        basePath = Path(__file__).parent.parent
        logging.basicConfig(filename= basePath  / 'Logger/automation.log', format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M: %S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
