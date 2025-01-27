import os

" Define the path of the training FILE "


ARTIFACTS_PATH = 'Artifacts'
DATA_FILE_PATH = r'D:\assamement-project\End-to-End-Sentiment-Analysis\data\dataset.csv'
DATA_NAME:str= 'raw.csv'

TRANING_FILE_NAME = 'Train.csv'
TESTING_FILE_NAME = 'Test.csv'
VALIDATION_FILE_NAME = 'Validation.csv'

" Define the path of the schema file "
SCHEMA_File_DIR: str='schema_data'
SCHEMA_File_NAME: str='schema.yaml'

"""preprocessing constants"""
PREPROCESSING_COLUMN:str='review_text'
PREPROCESSING_OBJECT_DIR:str='preprocesser'
PREPROCESSING_OBJECT_NAME:object='preprocess_text.pkl'

"""Target Column"""
TARGET_COLUMN:str='sentiment'

"""Model constants"""
MODEL_DIR:str='model'
MODEL_FILE:str='model.pkl'



" Define Data Ingestion Constants"
DATA_INGESTION_DIR_NAME: str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION__DIR:str='ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.20
DATA_INGESTION_TRAIN_VALIDATION_SPLIT_RATIO:float=0.20

""" Data VALIDATION related constants """

DATA_VALIDATION_DIR_NAME:str='data_validation'
DATA_VALIDATION_VALID_DIR:str='validated'
DATA_VALIDATION_INVALID_DIR:str='invalid'
DATA_VALIDATION_DRIFT_REPORT_DIR:str='validation_report'
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str='report.yaml'

""" Data Transformation related constants """
DATA_TRANSFORMATION_DIR_NAME:str='data_transformation'
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str='transformed'
DATA_TRANSFORMATION_TRANSFORMED_TEST_FILE_NAME:str='test.npy'
DATA_TRANSFORMATION_TRANSFORMED_TRAIN_FILE_NAME:str='train.npy'
DATA_TRANSFORMATION_TRANSFORMED_VALID_FILE_NAME:str='valid.npy'

"""Model Traning Constans """
MODEL_TRINER_DIR_NAME:str="model_trainer"
MODEL_TRINER_MODEL_METRICS_DIR:str="metrics"
MODEL_TRINER_MODEL_TRAIN_METRICS_FILE:str="train_metrics.json"
MODEL_TRINER_MODEL_TEST_METRICS_FILE:str="evaluation_metrics.json"
