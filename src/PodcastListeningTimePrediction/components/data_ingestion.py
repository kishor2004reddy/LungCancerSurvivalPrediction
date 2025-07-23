from PodcastListeningTimePrediction import logger
from PodcastListeningTimePrediction.entity.config_entity import DataIngestionConfig
from zipfile import ZipFile

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def extract_zip(self) -> None:
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        with ZipFile(self.config.zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)  
        logger.info(f"Data unzipped to {self.config.unzip_dir}")