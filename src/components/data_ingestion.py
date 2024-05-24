from src.entity import * 
from src.config import * 
from src.constants import * 
from src.utils import *
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np 

class Data_ingestion:
    def __init__(self):
        pass 

    def ingestion_start(self,data:ingestion):

        data_path=Path("artifacts/UpdatedResumeDataSet.csv")

        df=pd.read_csv(data_path)

        train_data,test_data=train_test_split(df,random_state=42,test_size=0.2)

        train_data.to_csv(data.train_dat)

        test_data.to_csv(data.test_data)


        return (data.train_dat,
                data.test_data)

