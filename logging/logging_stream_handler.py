import logging

logger = logging.getLogger('stream_logger')
logger.setLevel(logging.INFO)

console = logging.StreamHandler()

logger.addHandler(console)
logger.info("This is an informational message")