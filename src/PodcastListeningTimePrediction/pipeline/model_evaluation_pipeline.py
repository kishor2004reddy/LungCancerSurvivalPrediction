from PodcastListeningTimePrediction.components.model_evaluation import ModelEvaluation
from PodcastListeningTimePrediction.config.configuration import ConfigurationManager

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate_model()

