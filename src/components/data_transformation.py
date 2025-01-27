import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from src.logging.logger import logging
from src.utils.utils import save_obj, preprocess_text, save_numpy_arr
from src.entity.config_entity import DataTransformationConfig
from src.entity.artifacts_entity import DataTransformationArtifact, DataValidationArtifact
from src.constant.traning_pipline import TARGET_COLUMN, PREPROCESSING_COLUMN


class DataTransformation:
    def __init__(self, data_validation_artifacts: DataValidationArtifact,
                 data_transformation_config: DataTransformationConfig) -> None:
        self.data_validation_artifacts = data_validation_artifacts
        self.data_transformation_config = data_transformation_config

    @staticmethod
    def read_data(file_path: str) -> pd.DataFrame:
        return pd.read_csv(file_path)

    def initate_data_transformation(self) -> DataTransformationArtifact:
        try:
            # Load data paths
            train_data_path = self.data_validation_artifacts.valid_train_path
            test_data_path = self.data_validation_artifacts.valid_test_path
            valid_data_path = self.data_validation_artifacts.valid_train_path  #

            # Read datasets
            train_df = self.read_data(train_data_path)
            test_df = self.read_data(test_data_path)
            valid_df = self.read_data(valid_data_path)
            logging.info('Data successfully read.')

            # Validate required columns
            for df, name in [(train_df, 'Train'), (test_df, 'Test'), (valid_df, 'Validation')]:
                if PREPROCESSING_COLUMN not in df.columns or TARGET_COLUMN not in df.columns:
                    raise KeyError(f"Missing required columns in {name} dataset.")
                
            # Text preprocessing
            train_df[PREPROCESSING_COLUMN]=preprocess_text(train_df,PREPROCESSING_COLUMN)
            test_df[PREPROCESSING_COLUMN]=preprocess_text(test_df,PREPROCESSING_COLUMN)
            valid_df[PREPROCESSING_COLUMN]=preprocess_text(valid_df,PREPROCESSING_COLUMN)

            # TF-IDF Vectorization
            vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
            input_feature_train = vectorizer.fit_transform(train_df[PREPROCESSING_COLUMN]) # x_train
            input_feature_test = vectorizer.transform(test_df[PREPROCESSING_COLUMN]) # x_test
            input_feature_valid = vectorizer.transform(valid_df[PREPROCESSING_COLUMN]) # x_val

            # Targets
            target_feature_train = np.array(train_df[TARGET_COLUMN]) # y_train
            target_feature_test = np.array(test_df[TARGET_COLUMN]) # y_test
            target_feature_valid = np.array(valid_df[TARGET_COLUMN]) # y_val

            logging.info('Data preprocessing completed.')

            # Save transformed datasets
            train_arr = np.c_[input_feature_train.toarray(), target_feature_train]
            save_numpy_arr(self.data_transformation_config.transformed_train_file_path, train_arr)

            test_arr = np.c_[input_feature_test.toarray(), target_feature_test]
            save_numpy_arr(self.data_transformation_config.transformed_test_file_path, test_arr)

            valid_arr = np.c_[input_feature_valid.toarray(), target_feature_valid]
            save_numpy_arr(self.data_transformation_config.data_transformation_valid_file_path, valid_arr)

            # Save preprocessing object
            dir_path = os.path.dirname(self.data_transformation_config.preprocessing_object)
            os.makedirs(dir_path, exist_ok=True)
            save_obj(
                file_path=self.data_transformation_config.preprocessing_object,
                obj=vectorizer
            )
            logging.info('Preprocessor saved successfully.')

            # Create and return artifact
            data_transformation_artifact = DataTransformationArtifact(
                transformed_train_path=self.data_transformation_config.transformed_train_file_path,
                transformed_valid_path=self.data_transformation_config.data_transformation_valid_file_path,
                transformed_test_path=self.data_transformation_config.transformed_test_file_path,
                preprocess_obj=self.data_transformation_config.preprocessing_object
            )
            logging.info('Data transformation artifacts created successfully.')

            return data_transformation_artifact

        except Exception as e:
            logging.exception('Error during data transformation.')
            raise e
