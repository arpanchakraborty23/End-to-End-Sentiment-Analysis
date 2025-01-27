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