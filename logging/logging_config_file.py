import logging
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("exampleApp")

logger.info("Program started")
logger.info("Done!")