from src.entity import * 
from src.config import * 
from src.constants import * 
from src.utils import *
from pathlib import Path
import pandas as pd 
import numpy as np 
from sklearn.metrics import accuracy_score,classification_report
import dill
from sklearn.neighbors import KNeighborsClassifier
import nltk 
from sklearn.feature_extraction.text import TfidfVectorizer 







# compoenents 
class Model_training_:
    def __init__(self,config:model_training):
        self.config=config

    def model_training_start(self):
        X_train=pd.read_csv("artifacts/transformation/train.csv")
        X_test=pd.read_csv("artifacts/transformation/test.csv")
        
        self.tf=TfidfVectorizer()
        x_vectorized_train=self.tf.fit_transform(X_train["Resume"]).toarray()
        x_vectorized_test=self.tf.fit_transform(X_test["Resume"]).toarray()



        y_train=X_train["Category"]
        y_test=X_test["Category"]

        X_train,X_test,y_train,y_test=x_vectorized_train,x_vectorized_test,y_train,y_test

        self.kn=KNeighborsClassifier()
        self.kn.fit(X_train,y_train)

        self.pred=self.kn.predict(X_test)

        self.y_test=y_test


    def model_score(self):
        print(accuracy_score(self.pred,self.y_test))
        print(classification_report(self.pred,self.y_test))

    
    def save_vectorizer(self):
        with open(self.config.saved_vector_model,"wb") as file:
            dill.dump(self.tf,file)

    def save_model(self):
        with open(self.config.saved_model,"wb") as f:
            dill.dump(self.kn,f)
        
        