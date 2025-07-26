from PodcastListeningTimePrediction import logger
from PodcastListeningTimePrediction.entity.config_entity import DataTransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split
import os

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.dataframe = pd.read_csv(self.config.data_path)
    
    def drop_duplicates(self) -> None:
        """
        Drops duplicate rows from the dataframe
        Function returns None
        """
        initial_shape = self.dataframe.shape
        self.dataframe.drop_duplicates(inplace=True)
        final_shape = self.dataframe.shape
        logger.info(f"Dropped {initial_shape[0] - final_shape[0]} duplicate rows")
    
    def clean_data(self) -> None:
        """
        Cleans the data and saves it to the specified path
        Function returns None
        """
        self.dataframe.dropna(subset=["Listening_Time_minutes"], inplace=True)
        self.dataframe["Episode_Length_minutes"] = self.dataframe["Episode_Length_minutes"].fillna(self.dataframe["Episode_Length_minutes"].median())
        self.dataframe["Guest_Popularity_percentage"] = self.dataframe["Guest_Popularity_percentage"].fillna(self.dataframe["Guest_Popularity_percentage"].median())
        logger.info(f"Data cleaned")
    
    def split_data(self) -> None:
        """
        Splits the dataframe into training and testing sets
        Function returns None
        """

        train, test = train_test_split(self.dataframe, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info(f"Data split into train and test sets with shapes: {train.shape}, {test.shape}")