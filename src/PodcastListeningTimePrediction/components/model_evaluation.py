from PodcastListeningTimePrediction import logger
from PodcastListeningTimePrediction.entity.config_entity import ModelEvaluationConfig
import pandas as pd
from tensorflow.keras.models import load_model

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate_model(self):
        
        """Evaluate the trained model on the test dataset and save metrics."""

        # Load the model
        model = load_model(self.config.model_path)

        # Load the test data
        test_data = pd.read_csv(self.config.test_data_path)
        X_test = test_data.drop(columns=[self.config.target_column])
        y_test = test_data[self.config.target_column]

        # Evaluate the model
        loss, rmse = model.evaluate(X_test, y_test, verbose=0)
        
        # Prepare metrics
        metrics = {
            "loss": loss,
            "RootMeanSquaredError": rmse
        }

        # Save metrics to file
        with open(self.config.metric_file_path, 'w') as f:
            f.write(str(metrics))

        logger.info(f"Model evaluation metrics: {metrics}")