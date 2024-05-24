from src.components import *
from src.entity import * 
from src.config import * 
from src.constants import * 
from src.utils import * 




class Transformation:
    def __init__(self):
        pass 

    def main(self):
        a=Configuration_Manager()
        v=a.trasformation_config()
        z=Data_transformation(v)
        z.remvoing_unwanted_columns()
        z.comp_transformation()
