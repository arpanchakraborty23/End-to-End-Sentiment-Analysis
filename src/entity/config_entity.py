from datetime import datetime
import os
from src.constant import traning_pipline

class TraningPiplineConfig:
    def __init__(self)-> None:
        self.timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        self.artifacts_path = os.path.join(traning_pipline.ARTIFACTS_PATH, self.timestamp)

class DataIngestionConfig:
    def __init__(self, traning_pipline_config: TraningPiplineConfig)-> None:

        self.data_ingestion_dir = os.path.join(
            traning_pipline_config.artifacts_path, traning_pipline.DATA_INGESTION_DIR_NAME  ## creating data ingestion dir inside artifacts
         )
        self.data_ingestion_feature_store_dir = os.path.join(
            self.data_ingestion_dir, traning_pipline.DATA_NAME #  ## saving raw data in artifact with file name
         ) 
        self.data_ingestion_train_data_store_dir = os.path.join(
            self.data_ingestion_dir, traning_pipline.DATA_INGESTION_FEATURE_STORE_DIR,traning_pipline.DATA_TRANSFORMATION_TRANSFORMED_TRAIN_FILE_NAME #  artifacts folder , ingest folder , train data pat
        ) 
        self.data_ingestion_test_data_store_dir = os.path.join(
            self.data_ingestion_dir,traning_pipline.DATA_INGESTION_FEATURE_STORE_DIR, traning_pipline.TESTING_FILE_NAME ## artifacts folder , ingest folder , test data path
        )
        self.data_ingestion_valid_data_store_dir= os.path.join(
            self.data_ingestion_dir,traning_pipline.DATA_INGESTION_FEATURE_STORE_DIR,traning_pipline.VALIDATION_FILE_NAME ## artifacts folder , ingest folder , valid data path
        )
        self.data_ingestion_train_test_split_ratio = traning_pipline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO # 0.20
        self.data_ingestion_train_validation_split_ratio = traning_pipline.DATA_INGESTION_TRAIN_VALIDATION_SPLIT_RATIO # 0.20

class DataValidationConfig:
    def __init__(self,traning_pipline_config:TraningPiplineConfig) -> None:
      self.data_validation_dir:str=os.path.join(
      	traning_pipline_config.artifacts_path,traning_pipline.DATA_VALIDATION_DIR_NAME ## crating data validaton folder inside artifacts
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
         self.valid_dir_name, traning_pipline.TRANING_FILE_NAME  ## artifacts folder , ingest folder , train data path
		)
      self.valid_test_data_store_path:str=os.path.join(
         self.valid_dir_name,traning_pipline.TESTING_FILE_NAME ## artifacts folder , ingest folder , test data path
		)
      self.invalid_traning_data_store_path:str=os.path.join(
         self.valid_dir_name, traning_pipline.TRANING_FILE_NAME  ## artifacts folder , ingest folder , train data path
      )
      self.invalid_traning_data_store_path:str=os.path.join(
         self.valid_dir_name, traning_pipline.TRANING_FILE_NAME  ## artifacts folder , ingest folder , train data path
		)
      self.invalid_test_data_store_path:str=os.path.join(
         self.valid_dir_name, traning_pipline.TESTING_FILE_NAME ## artifacts folder , ingest folder , test data path
		)
      self.schema_file_path = os.path.join(
         traning_pipline.SCHEMA_File_DIR,traning_pipline.SCHEMA_File_NAME # schema file dir
      )

class DataTransformationConfig:
    def __init__(self, traning_pipline_config: TraningPiplineConfig) -> None:
        self.data_transformation_dir = os.path.join(
            traning_pipline_config.artifacts_path, traning_pipline.DATA_TRANSFORMATION_DIR_NAME # artifacts folder, data transformation folder
         )
        self.transformed_train_file_path = os.path.join(
               self.data_transformation_dir,traning_pipline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, traning_pipline.DATA_TRANSFORMATION_TRANSFORMED_TRAIN_FILE_NAME # transformed folder, train file name
         )
        self.transformed_test_file_path = os.path.join(  
               self.data_transformation_dir,traning_pipline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, traning_pipline.DATA_TRANSFORMATION_TRANSFORMED_TEST_FILE_NAME # transformed folder, test file name
         )
        self.data_transformation_valid_file_path = os.path.join(
               self.data_transformation_dir,traning_pipline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, traning_pipline.DATA_TRANSFORMATION_TRANSFORMED_VALID_FILE_NAME # transformed folder, valid file name
         )
        self.preprocessing_object = os.path.join(
            traning_pipline.PREPROCESSING_OBJECT_DIR,traning_pipline.PREPROCESSING_OBJECT_NAME # preprocesser folder, preprocesser object
        )

class ModelTrainerConfig:
    def __init__(self,traning_pipline_config:TraningPiplineConfig) -> None:
         self.model_trainer_dir = os.path.join(
               traning_pipline_config.artifacts_path, traning_pipline.MODEL_TRINER_DIR_NAME # artifacts folder, model trainer folder
         )
         self.model_obj_path= os.path.join(
               traning_pipline.MODEL_DIR ,traning_pipline.MODEL_FILE # model trainer folder, model folder
         )
         self.model_metrics_dir = os.path.join(
               self.model_trainer_dir, traning_pipline.MODEL_TRINER_MODEL_METRICS_DIR # model trainer folder, model metrics folder
         )
         self.train_metrics_file = os.path.join(
               self.model_metrics_dir, traning_pipline.MODEL_TRINER_MODEL_TRAIN_METRICS_FILE # model metrics folder, train metrics file
         )
         self.test_metrics_file = os.path.join(
               self.model_metrics_dir, traning_pipline.MODEL_TRINER_MODEL_TEST_METRICS_FILE # model metrics folder, test metrics file
         )
        