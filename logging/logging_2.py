import logging

# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", level=logging.INFO)

logging.debug("This is a debug message") # This one won't log
logging.info("Informational message")
logging.error("An error has happened!")