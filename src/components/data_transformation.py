import os
import sys
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from src.logging.logger import logging
from src.utils.utils import save_obj,save_numpy_arr,preprocess_text
from src.entity.config_entity import DataTransformationConfig
from src.entity.artifacts_entity import DataTransformationArtifact,DataValidationArtifact
from src.constant.traning_pipline import TARGET_COLUMN,PREPROCESSING_COLUMN



class DataTransformation:
    def __init__(self,data_validation_artifacts:DataValidationArtifact,
                 data_transformation_config:DataTransformationConfig) -> None:
        self.data_validation_artifacts=data_validation_artifacts
        self.data_transformaation_config=data_transformation_config

    @staticmethod
    def read_data(data: str)-> pd.DataFrame:
        return pd.read_csv(data)

    def initate_data_transformation(self)->DataTransformationArtifact:
        try:
            # load data
            train_data_path=self.data_validation_artifacts.valid_train_path
            test_data_path=self.data_validation_artifacts.valid_test_path
            valid_data_path=self.data_validation_artifacts.valid_train_path
            
            # read data
            train_df=self.read_data(data=train_data_path)
            test_df=self.read_data(data=test_data_path)
            valid_df=self.read_data(data=valid_data_path)
            logging.info('data read completed')
            print(train_df.head())

            # apply preprocessing
            train_df[PREPROCESSING_COLUMN]=train_df[PREPROCESSING_COLUMN].apply(preprocess_text)
            test_df[PREPROCESSING_COLUMN]=test_df[PREPROCESSING_COLUMN].apply(preprocess_text)
            valid_df[PREPROCESSING_COLUMN]=valid_df[PREPROCESSING_COLUMN].apply(preprocess_text)

            ## traning dataframe
            input_feature_train_df=train_df.drop(columns=[TARGET_COLUMN],axis=1) # x_train

            Target_feature_train_df=train_df[TARGET_COLUMN] # y_train
            Target_feature_train_df=Target_feature_train_df.replace(-1,0)

            ## test dataframe
            input_feature_test_df=test_df.drop(columns=[TARGET_COLUMN],axis=1) # x_test
            Target_feature_test_df=test_df[TARGET_COLUMN]
            Target_feature_test_df=Target_feature_test_df.replace(-1,0)

            ## validation dataframe
            input_feature_valid_df=valid_df.drop(columns=[TARGET_COLUMN],axis=1) # x_valid
            Target_feature_valid_df=valid_df[TARGET_COLUMN]
            Target_feature_valid_df=Target_feature_valid_df.replace(-1,0)

            ## Apply TF-IDF
            preprocess_obj=TfidfVectorizer(max_features=5000)

            transform_input_feature_train_df=preprocess_obj.fit_transform(input_feature_train_df)
            transform_input_feature_test_df=preprocess_obj.transform(input_feature_test_df)
            transform_input_feature_valid_df=preprocess_obj.transform(input_feature_valid_df)

            logging.info('data preprocessing completed')

            train_arr=np.c_[transform_input_feature_train_df,np.array(Target_feature_train_df)]
            save_numpy_arr(file=self.data_transformaation_config.data_transformation_train_path,arr=train_arr)

            test_arr=np.c_[transform_input_feature_test_df,np.array(Target_feature_test_df)]
            save_numpy_arr(file=self.data_transformaation_config.data_transformation_test_path,arr=test_arr)

            valid_arr=np.c_[transform_input_feature_valid_df,np.array(Target_feature_valid_df)]

            save_obj(
                file_path=self.data_transformaation_config.preprocessing_object,
                obj=preprocess_obj
            )
            
            ## final model
            save_obj(file_path='final_model/preprocesser.pkl',obj=preprocess_obj)
            print('preprocesser save successfully')
            data_transformation_artifacts=DataTransformationArtifact(
                train_arr_path=self.data_transformaation_config.transformed_train_file_path,
                test_arr_path=self.data_transformaation_config.transformed_test_file_path,
                valid_arr_path=self.data_transformaation_config.data_transformation_valid_file_path,
                preprocess_obj_path=self.data_transformaation_config.preprocessing_object
            )
            print('Data transformation artifacts created')
            logging.info('Data transformation artifacts created')
            
            return data_transformation_artifacts

        except Exception as e:
            logging.info(f'Error in Data transformation {str(e)}')
            print(e)