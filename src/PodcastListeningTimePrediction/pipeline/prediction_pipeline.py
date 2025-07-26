from tensorflow.keras.models import load_model
from PodcastListeningTimePrediction.components.data_transformation import DataTransformation
from PodcastListeningTimePrediction.config.configuration import ConfigurationManager
import pandas as pd
import joblib
from PodcastListeningTimePrediction.components.preprocessor import PodcastPreprocessor

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager()
        self.model = load_model(self.config.config.model_training.model_path)
        self.preprocessor = joblib.load(self.config.config.model_training.preprocessor_path)
    
    
    def make_input_df(
        self,
        *,
        Podcast_Name: str,
        Episode_Title: str,
        Episode_Length_minutes: float,
        Genre: str,
        Host_Popularity_percentage: float,
        Publication_Day: str,
        Publication_Time: str,
        Guest_Popularity_percentage: float,
        Number_of_Ads: int,
        Episode_Sentiment: str
    ) -> pd.DataFrame:
        columns = [
            "Podcast_Name",
            "Episode_Title",
            "Episode_Length_minutes",
            "Genre",
            "Host_Popularity_percentage",
            "Publication_Day",
            "Publication_Time",
            "Guest_Popularity_percentage",
            "Number_of_Ads",
            "Episode_Sentiment"
        ]
        values = [[
            Podcast_Name, Episode_Title, Episode_Length_minutes, Genre, Host_Popularity_percentage,
            Publication_Day, Publication_Time, Guest_Popularity_percentage, Number_of_Ads, Episode_Sentiment
        ]]
        return pd.DataFrame(values, columns=columns)
    
    def predict(
        self,
        *,
        Podcast_Name: str,
        Episode_Title: str,
        Episode_Length_minutes: float,
        Genre: str,
        Host_Popularity_percentage: float,
        Publication_Day: str,
        Publication_Time: str,
        Guest_Popularity_percentage: float,
        Number_of_Ads: int,
        Episode_Sentiment: str
    ) -> float:
        """
        Predict the listening time for a given input data.

        Returns:
            float: Predicted listening time.
        """
        input_df = self.make_input_df(
            Podcast_Name=Podcast_Name,
            Episode_Title=Episode_Title,
            Episode_Length_minutes=Episode_Length_minutes,
            Genre=Genre,
            Host_Popularity_percentage=Host_Popularity_percentage,
            Publication_Day=Publication_Day,
            Publication_Time=Publication_Time,
            Guest_Popularity_percentage=Guest_Popularity_percentage,
            Number_of_Ads=Number_of_Ads,
            Episode_Sentiment=Episode_Sentiment
        )

        # Preprocess input
        processed_df = self.preprocessor.transform(input_df)

        prediction = self.model.predict(processed_df)
        return float(prediction[0][0])






