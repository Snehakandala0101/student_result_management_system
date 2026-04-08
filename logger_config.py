import logging
import os

#create logs folder if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")

logger=logging.getLogger("SRMS")
logger.setLevel(logging.DEBUG)

file_handler=logging.FileHandler("logs/system.log")
formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

file_handler.setFormatter(formatter)

if not logger.handlers:
    logger.addHandler(file_handler)