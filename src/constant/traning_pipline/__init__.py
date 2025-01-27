import os

" Define the path of the training FILE "

ARTIFACTS_PATH = 'Artifacts'
DATA_FILE_PATH = 'Data.CSV'

TRANING_FILE_PATH = 'Train.csv'
TESTING_FILE_PATH = 'Test.csv'
VALIDATION_FILE_PATH = 'Validation.csv'

" Define the path of the schema file "
SCHEMA_File_DIR: str='schema_data'
SCHEMA_File_NAME: str='schema.yaml'

"""preprocessing constants"""
PREPROCESSING_COLUMN:str='clean_text'
PREPROCESSING_Object:str='preprocess_text'

"""Target Column"""
TARGET_COLUMN:str='sentiment'




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
