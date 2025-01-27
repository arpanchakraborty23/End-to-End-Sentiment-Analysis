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

class DataValidationConfig:
    def __init__(self,traning_pipline_config:TraningPiplineConfig) -> None:
      self.data_validation_dir:str=os.path.join(
      	traning_pipline_config.artifact_dir,traning_pipline.DATA_VALIDATION_DIR_NAME ## crating data validaton folder inside artifacts
		)
      self.valid_dir_name:str=os.path.join(
         self.data_validation_dir, traning_pipline.DATA_VALIDATION_VALID_DIR ## validated report folder inside data validation folder
		)
      self.invalid_dir_name:str=os.path.join(
         self.data_validation_dir,traning_pipline.DATA_VALIDATION_INVALID_DIR ## invalid report folder inside data validation folder
		)
      self.drift_report_dir:str=os.path.join(
         self.data_validation_dir,traning_pipline.DATA_VALIDATION_DRIFT_REPORT_DIR,traning_pipline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME # data validation dir, drift report dir, report name
		)
      self.valid_traning_data_store_path:str=os.path.join(
         self.valid_dir_name, traning_pipline.TRAIN_FILE_NAME  ## artifacts folder , ingest folder , train data path
		)
      self.valid_test_data_store_path:str=os.path.join(
         self.valid_dir_name,traning_pipline.TEST_FILE_NAME ## artifacts folder , ingest folder , test data path
		)
      self.invalid_traning_data_store_path:str=os.path.join(
         self.valid_dir_name, traning_pipline.TRAIN_FILE_NAME  ## artifacts folder , ingest folder , train data path
      )
      self.invalid_traning_data_store_path:str=os.path.join(
         self.valid_dir_name, traning_pipline.TRAIN_FILE_NAME  ## artifacts folder , ingest folder , train data path
		)
      self.invalid_test_data_store_path:str=os.path.join(
         self.valid_dir_name, traning_pipline.TEST_FILE_NAME ## artifacts folder , ingest folder , test data path
		)
      self.schema_file_path = os.path.join(
         traning_pipline.SCHEMA_File_DIR,traning_pipline.SCHEMA_File_NAME # schema file dir
      )

class DataTransformationConfig:
    def __init__(self, traning_pipline_config: TraningPiplineConfig) -> None:
        self.data_transformation_dir = os.path.join(
            traning_pipline_config.artifacts_path, traning_pipline.DATA_TRANSFORMATION_DIR_NAME # artifacts folder, data transformation folder
         )
        self.transformed_data_dir = os.path.join(
               self.data_transformation_dir, traning_pipline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR # data transformation folder, transformed folder
         )
        self.transformed_train_file_path = os.path.join(
               self.transformed_data_dir, traning_pipline.DATA_TRANSFORMATION_TRANSFORMED_TRAIN_FILE_NAME # transformed folder, train file name
         )
        self.transformed_test_file_path = os.path.join(  
               self.transformed_data_dir, traning_pipline.DATA_TRANSFORMATION_TRANSFORMED_TEST_FILE_NAME # transformed folder, test file name
         )
        self.data_transformation_valid_file_path = os.path.join(
               self.transformed_data_dir, traning_pipline.DATA_TRANSFORMATION_TRANSFORMED_VALID_FILE_NAME # transformed folder, valid file name
         )
        self.preprocessing_object = traning_pipline.PREPROCESSING_Object # preprocess_text