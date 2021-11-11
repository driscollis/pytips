import logging

logging.basicConfig(filename="ex_logger.log")
log = logging.getLogger("ex")
log.setLevel(logging.INFO)
log.info("This is informational")