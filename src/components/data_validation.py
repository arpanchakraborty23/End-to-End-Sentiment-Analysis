from src.logging.logger import logging
import os
import sys
import numpy as np
import pandas as pd
from typing import List
from scipy.stats import ks_2samp
from src.utils.utils import read_yaml, write_yaml_file
from src.logging.logger import logging
from src.entity.artifacts_entity import DataIngestionArtifacts,DataValidationArtifact
from src.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, training_pipeline_config: DataValidationConfig, data_ingestion_artifacts: DataIngestionArtifacts) -> None:
        self.data_ingestion_artifacts = data_ingestion_artifacts
        self.data_validation_config = training_pipeline_config
        self.schema_config = read_yaml(self.data_validation_config.schema_file_path)

    @staticmethod
    def read_data(filepath: str) -> pd.DataFrame:
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            print(e)

    def validate_num_of_col(self, df: pd.DataFrame) -> bool:
        try:
           
             # checking 'Unnamed: 0' col prasent or not
            if 'Unnamed: 0' in df.columns:
                print('Unnamed: 0 present in dataframe')
                logging.info(f'Unnamed: 0 present in dataframe {df.columns}')
                df.drop(columns='Unnamed: 0',axis=1,inplace=True)
            else:
                df

            number_of_columns=len(self.schema_config['columns'])

            number_of_df_columns=len(df.columns)
            logging.info(f"Required number of columns:{number_of_columns}")
            logging.info(f"Data frame has columns:{number_of_df_columns}")
            if number_of_df_columns==number_of_columns:
                return True
            return False
        except Exception as e:
            print(e)

    def validate_numaric_cols(self, df: pd.DataFrame) -> bool:
        try:
            numerical_columns=len(self.schema_config['numarical_column'])
            
            # checking 'Unnamed: 0' col prasent or not
            if 'Unnamed: 0' in df.columns:
                print('Unnamed: 0 present in dataframe')
                logging.info(f'Unnamed: 0 present in dataframe {df.columns}')
                df.drop(columns='Unnamed: 0',axis=1,inplace=True)
            else:
                df
            print(df.info())
            numerical_columns_in_df=len(df.select_dtypes(include=int).columns)
            logging.info(f"Required number of numarical columns:{numerical_columns}")
            logging.info(f"Data frame has numarical columns:{numerical_columns_in_df}")
            if numerical_columns_in_df==numerical_columns:
                return True
            return False
        except Exception as e:
            print(e)

    def detect_data_drift(self, base_df: pd.DataFrame, current_df: pd.DataFrame, threshold: float = 0.05) -> bool:
        try:
            status = True
            report = {}

            for column in base_df.columns:
                d1=base_df[column]
                d2=current_df[column]
                _, p_value=ks_2samp(d1,d2)
                if threshold<=p_value:
                    is_found=False
                else:
                    is_found=True
                    status=False
                report.update({column:{
                    "p_value":float(p_value),
                    "drift_status":is_found
                    
                    }})

            drift_report_path = self.data_validation_config.drift_report_dir
            os.makedirs(os.path.dirname(drift_report_path), exist_ok=True)
            write_yaml_file(file_path=drift_report_path, content=report)

            logging.info('Data drift detection completed and report generated.')
            return status
        except Exception as e:
            print(e)

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifacts.train_data_path
            test_file_path = self.data_ingestion_artifacts.test_data_path
            val_file_path = self.data_ingestion_artifacts.validation_data_path

            # Read training and test data
            train_df = self.read_data(train_file_path)
            test_df = self.read_data(test_file_path)
            val_df = self.read_data(val_file_path)
            logging.info('Data read from training and test and vallid files completed.')

            # Validate number of columns
            if not self.validate_num_of_cols(df=train_df):
                raise("Training data does not contain the expected columns.")
            if not self.validate_num_of_cols(df=test_df):
                raise("Testing data does not contain the expected columns.")
            if not self.validate_num_of_cols(df=val_df):
                raise("Validation data does not contain the expected columns.")

            # validate number of nmarical cols
            if not self.validate_numaric_cols(df=train_df):
                raise('Training data does not contain the expected numarical columns.')
            if not self.validate_numaric_cols(df=test_df):
                raise("Testing data does not contain the expected numarical columns.")
            if not self.validate_numaric_cols(df=val_df):
                raise("Validation data does not contain the expected numarical columns.")
            

            
            # Check for data drift
            drift_status = self.detect_data_drift(base_df=train_df, current_df=test_df)
            drift_status = self.detect_data_drift(base_df=train_df, current_df=val_df)

            logging.info('data dreft report created successfully')
            print('data dreft report created successfully')

            # Save validated data
            dir_path=os.path.dirname(self.data_validation_config.valid_traning_data_store_path)
            os.makedirs(dir_path,exist_ok=True)

            train_df.to_csv(
                self.data_validation_config.valid_traning_data_store_path,index=False, header=True
            )

            dir_path=os.path.dirname(self.data_validation_config.valid_test_data_store_path)
            os.makedirs(dir_path,exist_ok=True)
            test_df.to_csv(
                self.data_validation_config.valid_test_data_store_path, index=False, header=True
                )
            
            dir_path=os.path.dirname(self.data_validation_config.valid_test_data_store_path)
            os.makedirs(dir_path,exist_ok=True)
            val_df.to_csv(self.data_validation_config.valid_test_data_store_path, index=False, header=True)

            # Create DataValidationArtifact
            data_validation_artifact = DataValidationArtifact(
                validation_status=drift_status,
                valid_train_path=self.data_validation_config.valid_traning_data_store_path,
                valid_test_path=self.data_validation_config.valid_test_data_store_path,
                invalid_train_path=None,
                invalid_test_path=None,
                drift_report_path=self.data_validation_config.drift_report_dir
            )
            logging.info('Data validation completed successfully.')
            return data_validation_artifact
        except Exception as e:
            print(e)