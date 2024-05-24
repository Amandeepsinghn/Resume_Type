import os 
import sys 
from src.constants import *
from dataclasses import dataclass
from src.utils import * 
from pathlib import Path 


#entity 
@dataclass
class ingestion:
    root_dir: Path 
    test_data: Path 
    train_dat: Path


@dataclass
class transformation:
  root_dir: Path
  transformed_train_data: Path
  transformed_test_data: Path
  transformation_pickle_file: Path 


@dataclass
class model_training:
    root_dir: Path 
    saved_model: Path

  