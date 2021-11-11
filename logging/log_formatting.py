import logging

logger = logging.getLogger('stream_logger')
logger.setLevel(logging.INFO)

console = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
console.setFormatter(formatter)

logger.addHandler(console)
logger.info("This is an informational message")