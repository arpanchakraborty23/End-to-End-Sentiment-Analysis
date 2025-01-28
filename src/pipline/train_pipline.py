from src.logging.logger import logging
from src.entity.config_entity import TraningPiplineConfig, DataIngestionConfig, DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.constant import traning_pipline
from src.entity.artifacts_entity import DataIngestionArtifacts,DataValidationArtifact,DataTransformationArtifact,ModelTrainerArtifact
from src.cloud.s3_syncer import S3Sync

class TraningPipline:
    def __init__(self) -> None:
        self.traning_pipline_config=TraningPiplineConfig()
        self.s2_sync=S3Sync()

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
    def start_data_transformation(self,data_validation_artifact:DataValidationArtifact):
        try:
            logging.info(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Data Transformation Started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            data_transformation=DataTransformation()
            data_transformation.initate_data_transformation(data_validation_artifact=data_validation_artifact)
            data_transformation_artifact=data_transformation.initate_data_transformation()
            logging.info(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Data Transformation completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            return data_transformation_artifact
        except Exception as e:
            logging.info(f'Error in data transformation {str(e)}')
            print(e)


    def start_model_train(self,data_transformation_artifacts:DataTransformationArtifact):
        try:
            logging.info(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Model Train Started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            model_trainer_config=ModelTrainerConfig(traning_pipline_config=self.traning_pipline_config)
            model_trainer=ModelTrainer(
               model_trainer_config=model_trainer_config,
               data_transformation_artifacts=data_transformation_artifacts
                )
            model_trainer_artifacts=model_trainer.initiate_model_training()
            logging.info(f'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Model Train Completed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            return model_trainer_artifacts
            
        except Exception as e:
            logging.info(f'Error in model train {str(e)}')
            print(e)

    def sync_artifact_to_s3(self):
        try:
            aws_buket_url= f's3://{traning_pipline.TRANING_S3_BUCKER}/Artifacts/{self.traning_pipline_config.timestamp}'
            self.s2_sync.sync_folder_to_s3(folder=self.traning_pipline_config.artifacts_path,aws_bucket_url=aws_buket_url)
        except Exception as e:
            print(e)

    def sync_model_to_s3(self):
        try:
            aws_buket_url= f's3://{traning_pipline.TRANING_S3_BUCKER}/model/{self.traning_pipline_config.timestamp}'
            self.s2_sync.sync_folder_to_s3(folder=ModelTrainer().model_trainer_config.model_obj_path,aws_bucket_url=aws_buket_url)
        except Exception as e:
            print(e)

    def sync_preprocesser_to_s3(self):
        try:
            aws_buket_url= f's3://{traning_pipline.TRANING_S3_BUCKER}/preprcesser/{self.traning_pipline_config.timestamp}'
            self.s2_sync.sync_folder_to_s3(folder=DataTransformationConfig().data_transformation_config.preprocessing_object,aws_bucket_url=aws_buket_url)
        except Exception as e:
            print(e)

    def run(self):
        try:
            logging.info('************************************ Traning Pipline Started ************************************')
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifacts=data_ingestion_artifact)
            data_transformation_artifact=self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact=self.start_model_train(data_transformation_artifacts=data_transformation_artifact)
            self.sync_artifact_to_s3()
            self.sync_preprocesser_to_s3()
            self.sync_model_to_s3()

            logging.info('************************************ Traning Pipline Completed ************************************')
            return model_trainer_artifact

        except Exception as e:
            logging.info(f'Error in training pipeline {str(e)}')
            print(e)