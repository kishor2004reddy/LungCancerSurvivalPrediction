from LungCancerSurvivalPrediction.constants import *
from LungCancerSurvivalPrediction.utils.common import read_yaml, create_directories
from LungCancerSurvivalPrediction.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
            self,
            config_file_path=CONFIG_FILE_PATH,
            schema_file_path=SCHEMA_FILE_PATH,
            params_file_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.schema = read_yaml(schema_file_path)
        self.params = read_yaml(params_file_path)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        root_dir = self.config.data_ingestion.root_dir
        zip_file_path = self.config.data_ingestion.zip_file_path
        unzip_dir = self.config.data_ingestion.unzip_dir

        create_directories([Path(root_dir)])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(root_dir),
            zip_file_path=Path(zip_file_path),
            unzip_dir=Path(unzip_dir)
        )
        return data_ingestion_config