import logging
import logging.handlers

logger = logging.getLogger("email_logger")
logger.setLevel(logging.INFO)
fh = logging.handlers.SMTPHandler('smtp.my_server.com',
                                  fromaddr='log@my_server.com',
                                  toaddrs=['mike@my_server.com'],
                                  subject='Python log')
logger.addHandler(fh)
logger.info("This is an informational message")