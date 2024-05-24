from src.entity import * 
from src.config import * 
from src.constants import * 
from src.utils import *
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np 
import nltk 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
nltk.download("wordnet")



# components
class Data_transformation:
    def __init__(self,config:transformation):
        self.config=config

    def remvoing_unwanted_columns(self):
        self.df_train=pd.read_csv("artifacts/data_ingestion/train.csv")
        self.df_train.drop("Unnamed: 0",inplace=True,axis=1)
        self.df_test=pd.read_csv("artifacts/data_ingestion/test.csv")
        self.df_test.drop("Unnamed: 0",inplace=True,axis=1)
    

            
    def comp_transformation(self):
        corpus=[]
        wn=WordNetLemmatizer()
        for i in range(len(self.df_train)):
            sentence = re.sub("[^a-zA-Z]", " ", self.df_train['Resume'][i])
            sentence=sentence.lower()
            sentence=sentence.split()
            sentence=[wn.lemmatize(word) for word in sentence if word not in stopwords.words("english")]
            sentence=" ".join(sentence)
            corpus.append(sentence)
        
        self.df_train.drop("Resume",axis=1,inplace=True)

        self.df_train['Resume']=corpus

        cropus_1=[]
        for i in range(len(self.df_test)):
            sentence = re.sub("[^a-zA-Z]", " ", self.df_test['Resume'][i])
            sentence=sentence.lower()
            sentence=sentence.split()
            sentence=[wn.lemmatize(word) for word in sentence if word not in stopwords.words("english")]
            sentence=" ".join(sentence)
            cropus_1.append(sentence)
        
        self.df_test.drop("Resume",axis=1,inplace=True)

        self.df_test["Resume"]=cropus_1


        self.df_train["Category"]=self.df_train["Category"].map({'Data Science':0, 'HR':1, 'Advocate':2, 'Arts':3, 'Web Designing':4,
       'Mechanical Engineer':5, 'Sales':6, 'Health and fitness':7,
       'Civil Engineer':8, 'Java Developer':9, 'Business Analyst':10,
       'SAP Developer':11, 'Automation Testing':12, 'Electrical Engineering':13,
       'Operations Manager':14, 'Python Developer':15, 'DevOps Engineer':16,
       'Network Security Engineer':17, 'PMO':18, 'Database':19, 'Hadoop':20,
       'ETL Developer':21, 'DotNet Developer':22, 'Blockchain':23, 'Testing':24})

        self.df_test["Category"]=self.df_test["Category"].map({'Data Science':0, 'HR':1, 'Advocate':2, 'Arts':3, 'Web Designing':4,
       'Mechanical Engineer':5, 'Sales':6, 'Health and fitness':7,
       'Civil Engineer':8, 'Java Developer':9, 'Business Analyst':10,
       'SAP Developer':11, 'Automation Testing':12, 'Electrical Engineering':13,
       'Operations Manager':14, 'Python Developer':15, 'DevOps Engineer':16,
       'Network Security Engineer':17, 'PMO':18, 'Database':19, 'Hadoop':20,
       'ETL Developer':21, 'DotNet Developer':22, 'Blockchain':23, 'Testing':24})

        self.df_train.to_csv(self.config.transformed_train_data,index=False,header=True)
        self.df_train.to_csv(self.config.transformed_test_data,index=False,header=True)
