from PodcastListeningTimePrediction.config.configuration import ConfigurationManager
from PodcastListeningTimePrediction.components.data_validation import DataValidation


class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self): 
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config() 
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_data()