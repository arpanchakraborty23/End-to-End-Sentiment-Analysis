from datetime import datetime
import os
from src.constant import traning_pipline

class TraningPiplineConfig:
    def __init__(self)-> None:
        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.artifacts_path = os.path.join(traning_pipline.ARTIFACTS_PATH, self.timestamp)

class DataIngestionConfig:
    def __init__(self, traning_pipline_config: TraningPiplineConfig)-> None:
        self.data_ingestion_dir = os.path.join(traning_pipline.ARTIFACTS_PATH, traning_pipline.DATA_INGESTION_DIR_NAMR) # 'Artifacts/data_ingestion'
        self.data_ingestion_feature_store_dir = os.path.join(self.data_ingestion_dir, traning_pipline.DATA_INGESTION_FEATURE_STORE_DIR) # 'Artifacts/data_ingestion/feature_store
        self.data_ingestion_feature_store_dir = os.path.join(self.data_ingestion_dir, traning_pipline.DATA_INGESTION_FEATURE_STORE_DIR) # 'Artifacts/data_ingestion/feature_store
        self.data_ingestion_dir = os.path.join(self.data_ingestion_dir, traning_pipline.DATA_INGESTION__DIR) # 'Artifacts/data_ingestion/ingested'
        self.train_data_path:str= os.path.join(self.data_ingestion_dir, traning_pipline.TRANING_FILE_PATH) # 'Artifacts/data_ingestion/ingested/Train.csv'
        self.test_data_path:str= os.path.join(self.data_ingestion_dir, traning_pipline.TESTING_FILE_PATH) # 'Artifacts/data_ingestion/ingested/Test.csv'
        self.validation_data_path:str= os.path.join(self.data_ingestion_dir, traning_pipline.VALIDATION_FILE_PATH) # 'Artifacts/data_ingestion/ingested/Validation.csv'
        self.data_ingestion_train_test_split_ratio = traning_pipline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO # 0.20
        self.data_ingestion_train_validation_split_ratio = traning_pipline.DATA_INGESTION_TRAIN_VALIDATION_SPLIT_RATIO # 0.20