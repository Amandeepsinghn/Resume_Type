import os 
from pathlib import Path 
import logging 
import sys 


project_name="Resume_Type"


#list of files to make 
files=[
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/config/__init__.py",
    f"src/constants/__init__.py",
    f"src/entity/__init__.py",
    f"src/pipeline/__init__.py",
    f"src/utils/__init__.py",
    f".github/workflows/.gitkeep",
    f"config/config.yaml",
    f"research/trails.ipynb",
    f"setup.py",
    f"requirements.txt",
    f"params.yaml",
]


for file in files:
    file_path=Path(file)
    filedir,filename=os.path.split(file_path)

    if filedir!="":
        os.makedirs(filedir)


    if (not os.path.exists(filename)) or (os.path.getsize(filedir)==0):
        with open(file_path,"w") as f:
            pass

     