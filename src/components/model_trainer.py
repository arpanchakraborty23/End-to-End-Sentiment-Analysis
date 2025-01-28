import os
import sys
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB,GaussianNB
from sklearn.ensemble import RandomForestClassifier,BaggingClassifier
from dotenv import load_dotenv
load_dotenv()

from src.utils.utils import save_obj,save_as_json
from src.utils.model_utils import model_evaluatuion,get_classification_report
from src.logging.logger import logging
from src.entity.artifacts_entity import ModelTrainerArtifact,DataTransformationArtifact
from src.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self,model_trainer_config:ModelTrainerConfig,data_transformation_artifacts:DataTransformationArtifact) -> None:
        self.model_trainer_config=model_trainer_config
        self.data_transformation_artifacts=data_transformation_artifacts

 
    def train_model(self,x_train,y_train,x_valid,y_valid,x_test,y_test):
        try:
            logging.info('model training started')
            models = {
                      'LogisticRegression': LogisticRegression(),
                      'MultinomialNB': MultinomialNB(),
                      'GaussianNB': GaussianNB(),
                      'RandomForestClassifier': RandomForestClassifier(),
                    #   'BaggingClassifier': BaggingClassifier()
                      }
            
            report:dict=model_evaluatuion(x_train,y_train,x_valid,y_valid,models)
            print(report)

            logging.info('model training completed')
            logging.info(f'model report: {report}')

            print('*'*100)

            # find best traning model
            best_model_score=max(sorted(report.values()))
            best_model_name= list(report.keys())[
                list(report.values()).index(best_model_score)
            ]

            best_model=models[best_model_name]

            ## model training metrics
            y_train_pred=best_model.predict(x_train)
            traning_classification_metrics=get_classification_report(y_true=y_valid,y_pred=y_train_pred)

            save_as_json(
                obj=traning_classification_metrics,
                file_path=self.model_trainer_config.train_metrics_file
            )

            ## model evaluation metrics
            y_test_pred=best_model.predict(x_test)
            testing_classification_matrics=get_classification_report(y_true=y_test,y_pred=y_test_pred)
 
            save_as_json(
                obj=testing_classification_matrics,
                file_path=self.model_trainer_config.test_metrics_file
            )
            print('metrices track successfully')
            logging.info('Metrics save successfully')

            ## Seaving best model
            dir_path = os.path.dirname(self.model_trainer_config.model_obj_path)
            os.makedirs(dir_path, exist_ok=True)
            save_obj(
                obj=best_model,
                file_path=self.model_trainer_config.model_obj_path
            )
            logging.info(f'Model save in {self.model_trainer_config.model_obj_path}')
            return traning_classification_metrics,testing_classification_matrics

        except Exception as e:
            logging.info(f'error in model training {str(e)}')
            print(e)


    def initiate_model_training(self):
        try:
            logging.info('model training started')
            # load data
            train__array=np.load(self.data_transformation_artifacts.transformed_train_path)
            test_array=np.load(self.data_transformation_artifacts.transformed_test_path)
            valid_array=np.load(self.data_transformation_artifacts.transformed_valid_path)

            print(train__array)
            print(test_array)

            # split data
            x_train,y_train=train__array[:,:-1],train__array[:,-1]
            x_valid,y_valid=valid_array[:,:-1],valid_array[:,-1]
            x_test,y_test=test_array[:,:-1],test_array[:,-1]

            # model report
            
            traning_metrics,evaluation_metrics=self.train_model(x_train,y_train,x_valid,y_valid,x_test,y_test)

            mode_train_artifacts=ModelTrainerArtifact(
                model=self.model_trainer_config.model_obj_path,
                train_metrics_file=traning_metrics,
                test_metrics_file=evaluation_metrics
            )

            return mode_train_artifacts
        except Exception as e:
            print(e)