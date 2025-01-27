from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    train_data_path: str
    test_data_path: str
    validation_data_path: str


@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_path: str
    valid_test_path: str
    invalid_train_path: str
    invalid_test_path: str
    drift_report_path: str

@dataclass
class DataTransformationArtifact:
    transformed_train_path: str
    transformed_test_path: str
    transformed_valid_path: str
    preprocess_obj: object

@dataclass
class ModelTrainerArtifact:
    train_metrics_file: str
    test_metrics_file: str
    model: object

    