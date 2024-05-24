from src.components import *
from src.entity import * 
from src.config import * 
from src.constants import * 
from src.utils import * 


class Ingestion:
    def __init__(self):
        pass 


    def main(self):
        a=Configuration_Manager()
        c=a.ingestion_config()
        v=Data_ingestion()
        v.ingestion_start(c)

    