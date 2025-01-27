from src.logging.logger import logging
from src.entity.config_entity import TraningPiplineConfig, DataIngestionConfig, DataValidationConfig
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.constant import traning_pipline
from src.entity.artifacts_entity import DataIngestionArtifacts,DataValidationArtifact

class TraningPipline:
    def __init__(self) -> None:
        self.traning_pipline_config=TraningPiplineConfig()

    def start_data_ingestion(self):
        try:
            logging.info(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Data Ingestion Started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            start_data_ingestion_config=DataIngestionConfig(traning_pipline_config=self.traning_pipline_config)
            data_ingestion=DataIngestion(data_ingestion_config=start_data_ingestion_config)
            data_ingestion_artifats=data_ingestion.initiate_data_ingestion()

            logging.info(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Data Ingestion completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

            return data_ingestion_artifats
        except Exception as e:
            logging.info(f'Error in data ingestion {str(e)}')
            print(e)

    def start_data_validation(self,data_ingestion_artifats:DataIngestionArtifacts):
        try:
            logging.info(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Data Validation Started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            data_validation_config=DataValidationConfig(traning_pipline_config=self.traning_pipline_config)
            data_validation=DataValidation(training_pipeline_config=data_validation_config,data_ingestion_artifacts=data_ingestion_artifats)
            data_validation.initiate_data_validation()

            logging.info(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Data Validation completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

        except Exception as e:
            logging.info(f'Error in data validation {str(e)}')
            print(e)


    def run(self):
        try:
            logging.info('************************************ Traning Pipline Started ************************************')
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifacts=data_ingestion_artifact)
            


            logging.info('************************************ Traning Pipline Completed ************************************')

        except Exception as e:
            logging.info(f'Error in training pipeline {str(e)}')
            print(e)