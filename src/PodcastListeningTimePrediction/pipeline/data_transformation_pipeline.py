from PodcastListeningTimePrediction.config.configuration import ConfigurationManager
from PodcastListeningTimePrediction.components.data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self): 
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config() 
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.drop_duplicates()
        data_transformation.clean_data()
        data_transformation.split_data()