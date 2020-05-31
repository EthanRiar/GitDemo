import logging

logger = logging.getLogger(__name__)

fileHandler = logging.FileHandler('logfile.log')
logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")

logger.addHandler(fileHandler)
logger.debug("A debug statement is executed")
logger.info("Information message")
logger.warning("Something is in warning mode")
logger.error("Error!!!")
logger.critical("Critical issue")

