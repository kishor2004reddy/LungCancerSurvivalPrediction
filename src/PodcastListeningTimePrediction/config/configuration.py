from PodcastListeningTimePrediction.constants import *
from PodcastListeningTimePrediction.utils.common import read_yaml, create_directories
from PodcastListeningTimePrediction.entity.config_entity import *
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
    
    def get_data_validation_config(self) -> DataValidationConfig:
        
        config = self.config.data_validation
        


        create_directories([config.root_dir], verbose=True)

        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            unzip_data_path=Path(config.unzip_data_path),
            schema_file_path=Path(config.schema_file_path),
            report_file_path=Path(config.report_file_path)
        )
        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:

        config = self.config.data_transformation

        create_directories([config.root_dir], verbose=True)

        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path)
        )
        return data_transformation_config
    
    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.model_training

        create_directories([config.root_dir], verbose=True)

        model_training_config = ModelTrainingConfig(
            root_dir=Path(config.root_dir),
            train_data_path=Path(config.train_data_path),
            test_data_path=Path(config.test_data_path),
            model_path=config.model_path,
            target_column=list(self.schema.Target_Column.keys())[0]
        )
        return model_training_config
