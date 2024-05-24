from src.components import *
from src.entity import * 
from src.config import * 
from src.constants import * 
from src.utils import * 





class Training:
    def __init__(self):
        pass
    def main(self):

        a=Configuration_Manager()
        v=a.model_traning_config()
        z=Model_training_(v)
        z.model_training_start()
        z.model_score()
        z.save_model()
