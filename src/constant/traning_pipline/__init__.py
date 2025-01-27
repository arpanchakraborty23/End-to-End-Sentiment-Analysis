import os

" Define the path of the training FILE "

ARTIFACTS_PATH = 'Artifacts'
DATA_FILE_PATH = 'Data.CSV'

TRANING_FILE_PATH = 'Train.csv'
TESTING_FILE_PATH = 'Test.csv'
VALIDATION_FILE_PATH = 'Validation.csv'

" Define Data Ingestion Constants"
DATA_INGESTION_DIR_NAME: str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION__DIR:str='ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.20
DATA_INGESTION_TRAIN_VALIDATION_SPLIT_RATIO:float=0.20