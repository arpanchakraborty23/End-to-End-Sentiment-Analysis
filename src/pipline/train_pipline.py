from src.logging.logger import logging
from src.entity.config_entity import TraningPiplineConfig, DataIngestionConfig
from src.components.data_ingestion import DataIngestion
from src.constant import traning_pipline
from src.entity.artifacts_entity import DataIngestionArtifacts

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