import os
import sys
import yaml,json
import pandas as pd
import numpy as np
import pickle
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from box import ConfigBox
from src.logging.logger import logging


def read_yaml(file_path:str):
    try:
        with open(file_path) as f:
            file=yaml.safe_load(f)
        return ConfigBox(file)
    except Exception as e:
        logging.info(f'error in {str(e)}')
        print(e)
    
def write_yaml_file(file_path: str, content: object, replace: bool = False):
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        print(e)

def save_obj(obj, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f)

def preprocess_text(df,col):
   def clean_text(text):
        text=text.lower()
        text = re.sub(r'<[^>]*>', '', text) 
        text = re.sub(r'[^\w\s]', '', text)
        return text.strip()
   return df[col].map(clean_text)

def save_numpy_arr(file, arr):
    try:
        dir_path = os.path.dirname(os.path.abspath(file))
        os.makedirs(dir_path, exist_ok=True)
        # Save the numpy array
        with open(file, 'wb') as file:
            np.save(file, arr)
            print(f'Successfully saved array in {file}')
            logging.info(f'Successfully saved array in {file}')
            
    except Exception as e:
        print(e)
    
def load_numpy_arr(filepath):
    try:
        with open(filepath,'rb') as f:
            data=np.load(f,allow_pickle=True)
            logging.info(f'{data} load successfully ')
        return data
    except Exception as e:
        print(e)
    
def load_obj(file_path):
    with open(file_path,'rb') as f:
        data=pickle.load(f)

    return data


def save_as_json(obj, file_path):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'w') as f:
            json.dump(obj, f, indent=4)
    except Exception as e:
        logging(f"Error saving JSON to {file_path}: {e}")
        print(f"Error saving JSON to {file_path}: {e}")
        


