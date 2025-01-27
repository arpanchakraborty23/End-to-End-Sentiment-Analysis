import os
import sys
import yaml,json
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV
from pathlib import Path
from ensure import ensure_annotations
from box import ConfigBox
from sklearn.metrics import roc_auc_score,accuracy_score
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
 
    
def model_evaluatuion(x_train,y_train,x_test,y_test,models,prams):
    try:
            logging.info(' model evaluation started')
            report={}
            for i in range(len(models)):
                model = list(models.values())[i]
                param=prams[list(models.keys())[i]]
                #prams=prams[list(models.keys())[i]]
                print(f"Training {model}...")
                gs=GridSearchCV(model,param_grid=param,cv=5,verbose=3,refit=True,scoring='neg_mean_squared_error',n_jobs=-1)

            
                gs.fit(x_train,y_train)

                model.set_params(**gs.best_params_)

                # Train model
                model.fit(x_train,y_train)

                

                # Predict Testing data
                y_test_pred =model.predict(x_test)

                
                test_model_score = accuracy_score(y_test,y_test_pred)*100

                print(f"Training {model} accuracy {test_model_score}")

                report[list(models.keys())[i]] =  test_model_score

            return report
        
    except Exception as e:
        logging.info(f' Error {str(e)}')
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
        raise CustomException(e,sys)


