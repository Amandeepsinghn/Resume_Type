import os 
import sys 
from src.components import *
from src.entity import * 
from src.config import * 
from src.constants import * 
from src.utils import * 
import pytesseract
import cv2 
import dill 
import nltk
from dataclasses import dataclass
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
nltk.download("wordnet")


class Prediction:
    def __init__(self,image):
        self.image=image 

    def predict(self):
        original_image=cv2.imread(self.image)

        gray_image=cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)

        ocr=pytesseract.image_to_string(gray_image)


        corpus=[]
        wn=WordNetLemmatizer()
        sentence = re.sub("[^a-zA-Z]", " ", ocr)
        sentence=sentence.lower()
        sentence=sentence.split()
        sentence=[wn.lemmatize(word) for word in sentence if word not in stopwords.words("english")]
        sentence=" ".join(sentence)
        corpus.append(sentence)


        filepath="artifacts/trained_model/model.dill"
        with open(filepath,"rb") as f:
            model=dill.load(f)

        filepath="artifacts/trained_model/vector.dill"
        with open(filepath,"rb") as f:
            tf=dill.load(f)

        img=tf.transform(corpus)

        prediction=model.predict(img)

        prediction=prediction[0]

        if prediction == 0:
            return "Data Science"
        elif prediction == 1:
            return "HR"
        elif prediction == 2:
            return "Advocate"
        elif prediction == 3:
            return "Arts"
        elif prediction == 4:
            return "Web Designing"
        elif prediction == 5:
            return "Mechanical Engineer"
        elif prediction == 6:
            return "Sales"
        elif prediction == 7:
            return "Health and fitness"
        elif prediction == 8:
            return "Civil Engineer"
        elif prediction == 9:
            return "Java Developer"
        elif prediction == 10:
            return "Business Analyst"
        elif prediction == 11:
            return "SAP Developer"
        elif prediction == 12:
            return "Automation Testing"
        elif prediction == 13:
            return "Electrical Engineering"
        elif prediction == 14:
            return "Operations Manager"
        elif prediction == 15:
            return "Python Developer"
        elif prediction == 16:
            return "DevOps Engineer"
        elif prediction == 17:
            return "Network Security Engineer"
        elif prediction == 18:
            return "PMO"
        elif prediction == 19:
            return "Database"
        elif prediction == 20:
            return "Hadoop"
        elif prediction == 21:
            return "ETL Developer"
        elif prediction == 22:
            return "DotNet Developer"
        elif prediction == 23:
            return "Blockchain"
        elif prediction == 24:
            return "Testing"
        else:
            return "Unknown"    



        