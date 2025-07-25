from PodcastListeningTimePrediction.config.configuration import ConfigurationManager
from PodcastListeningTimePrediction.components.model_trainer import ModelTraining

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_training_config()
        model_trainer = ModelTraining(config=model_training_config)
        model_trainer.train_model()