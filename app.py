from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os 
from src.pipeline import Prediction
from src.utils.common import * 
from src.exception import *
import sys
from sqlalchemy import URL, create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# mysql+mysqlconnector://<username>:<password>@<host>:<port>/<dbname>
mysql_db_url = "mysql+mysqlconnector://root:Dklgbasant%4014@localhost:3306/googlyji"

engine=create_engine(mysql_db_url)

Base=declarative_base()

class User(Base):
    __tablename__="Resume"
    id=Column(Integer, primary_key=True,autoincrement=True)
    name=Column(String(20))
    email=Column(String(50))
    field=Column(String(20))

Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)

session=Session()



app=Flask(__name__)

class CleintApp:
    def __init__(self):
        self.image="input_image.jpg"
        self.classification=Prediction(self.image)



@app.route("/",methods=["GET","POST"])
def home_page():
    try:
        if request.method=="GET":
            return render_template("home.html")
        else:    
            name=request.form.get("name")
            email=request.form.get("email")
            image=request.files["image"]

            en_image=encode_image_to_base64(image)

            decodeImage(en_image,client.image)

            image=client.classification.predict()

            user=User(name=name,email=email,field=image)

            session.add(user)
            session.commit()
            session.close()

            return render_template("home.html",prediction=image)

            
    
    except Exception as e:
        raise(Custom_Exception(e,sys))


if __name__=="__main__":
    client=CleintApp()
    app.run(host="0.0.0.0",port=8080)
