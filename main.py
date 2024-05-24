from src.logger import logging 
from src.exception import Custom_Exception
from src.pipeline import Ingestion
from src.pipeline import Transformation
from src.pipeline import Training
import sys 
import os




try:
    logging.info("ingestion is started")
    a=Ingestion()
    a.main()
    logging.info("ingestion is completed")
except Exception as e:
    raise(Custom_Exception(e,sys))



try:
    logging.info("ingestion is started")
    b=Transformation()
    b.main()
    logging.info("ingestion is completed")
except Exception as e:
    raise(Custom_Exception(e,sys))



try:
    logging.info("training has started")
    c=Training()
    c.main()
    logging.info("training has been completed and best model has been saved")

except Exception as e:
    raise(Custom_Exception(e,sys))

