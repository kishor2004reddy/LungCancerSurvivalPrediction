from PodcastListeningTimePrediction import logger
from PodcastListeningTimePrediction.entity.config_entity import DataTransformationConfig
import pandas as pd
from sklearn.preprocessing import StandardScaler
from category_encoders import TargetEncoder
from sklearn.model_selection import train_test_split
import os
from pathlib import Path

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
    
    def create_features(self) -> None:
        """
        Creates new features based on existing data
        Function returns None
        """
        # Captures overall combined star power of the host and guest
        self.dataframe["Host_Guest_Combo_Popularity"] = self.dataframe["Host_Popularity_percentage"] * self.dataframe["Guest_Popularity_percentage"]

        # Normalizes ad count by episode length — a measure of ad density
        self.dataframe["Ads_per_Minute"] = self.dataframe["Number_of_Ads"] / (self.dataframe["Episode_Length_minutes"] + 0.00001)

        # Measures dominance of host popularity vs guest
        self.dataframe["Host_to_Guest_Popularity_Ratio"] = self.dataframe["Host_Popularity_percentage"]/ (self.dataframe["Guest_Popularity_percentage"] + 0.00001)

        # Difference in star power — useful if the gap impacts performance
        self.dataframe["Popularity_Difference"] = self.dataframe["Host_Popularity_percentage"] - self.dataframe["Guest_Popularity_percentage"]

        # Captures weighted presence of host/guest by episode duration
        self.dataframe["Length_x_Host_Popularity"] = self.dataframe["Episode_Length_minutes"] * self.dataframe["Host_Popularity_percentage"]
        self.dataframe["Length_x_Guest_Popularity"] = self.dataframe["Episode_Length_minutes"] * self.dataframe["Guest_Popularity_percentage"]

        # A rough proxy for how much value the show tries to extract (ads) based on star power
        self.dataframe["Ad_Density_Popularity"] = self.dataframe["Number_of_Ads"] * (self.dataframe["Host_Popularity_percentage"] + self.dataframe["Guest_Popularity_percentage"])

        # Weekend drops might behave differently in engagement
        self.dataframe["Weekend_Publication"] = self.dataframe["Publication_Day"].isin(["Saturday", "Sunday"]).astype(int)

    

    def scale_data(self) -> None:
        """
        Scales the numerical features in the dataframe
        Function returns None
        """
        scaler = StandardScaler()
        numerical_features = self.dataframe.select_dtypes(include=['float64', 'int64']).columns.tolist()
        
        self.dataframe[numerical_features] = scaler.fit_transform(self.dataframe[numerical_features])
        
        logger.info(f"Data scaled for features: {numerical_features}")

    def encode_data(self) -> None:
        """
        Encodes categorical features in the dataframe
        Function returns None
        """
        encoder = TargetEncoder() 
        categorical_features = self.dataframe.select_dtypes(include=['object']).columns.tolist()
        self.dataframe[categorical_features] = encoder.fit_transform(self.dataframe[categorical_features], self.dataframe["Listening_Time_minutes"])

        logger.info(f"Data encoded for features: {categorical_features}")

    def split_data(self) -> None:
        """
        Splits the dataframe into training and testing sets
        Function returns None
        """

        X = self.dataframe.drop(columns=["Listening_Time_minutes"])
        y = self.dataframe["Listening_Time_minutes"]
        
        train, test = train_test_split(self.dataframe, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info(f"Data split into train and test sets with shapes: {train.shape}, {test.shape}")