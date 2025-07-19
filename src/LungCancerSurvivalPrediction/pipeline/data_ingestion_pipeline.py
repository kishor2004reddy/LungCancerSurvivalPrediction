from LungCancerSurvivalPrediction.config.configuration import ConfigurationManager
from LungCancerSurvivalPrediction.components.data_ingestion import DataIngestion
from LungCancerSurvivalPrediction import logger

# import os
# from pathlib import Path

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self): 
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()  # Ensure to call the method
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.extract_zip()
    
        

    