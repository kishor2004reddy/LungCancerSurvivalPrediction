import pandas as pd
from sklearn.preprocessing import StandardScaler
from category_encoders import TargetEncoder
import numpy as np

class PodcastPreprocessor:
    def __init__(self):
        self.scaler = None
        self.encoder = None
        self.numerical_features = None
        self.categorical_features = None
        self.target_column = "Listening_Time_minutes"

    def fit(self, df: pd.DataFrame):
        df = df.copy()
        self.numerical_features = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        if self.target_column in self.numerical_features:
            self.numerical_features.remove(self.target_column)
        self.categorical_features = df.select_dtypes(include=['object']).columns.tolist()
        self.scaler = StandardScaler()
        self.encoder = TargetEncoder()
        self.scaler.fit(df[self.numerical_features])
        self.encoder.fit(df[self.categorical_features], df[self.target_column])
        return self

    def transform(self, df: pd.DataFrame):
        df = df.copy()
        # Feature engineering (repeat your logic here)
        df["Host_Guest_Combo_Popularity"] = df["Host_Popularity_percentage"] * df["Guest_Popularity_percentage"]
        df["Ads_per_Minute"] = df["Number_of_Ads"] / (df["Episode_Length_minutes"] + 0.00001)
        df["Host_to_Guest_Popularity_Ratio"] = df["Host_Popularity_percentage"] / (df["Guest_Popularity_percentage"] + 0.00001)
        df["Popularity_Difference"] = df["Host_Popularity_percentage"] - df["Guest_Popularity_percentage"]
        df["Length_x_Host_Popularity"] = df["Episode_Length_minutes"] * df["Host_Popularity_percentage"]
        df["Length_x_Guest_Popularity"] = df["Episode_Length_minutes"] * df["Guest_Popularity_percentage"]
        df["Ad_Density_Popularity"] = df["Number_of_Ads"] * (df["Host_Popularity_percentage"] + df["Guest_Popularity_percentage"])
        df["Weekend_Publication"] = df["Publication_Day"].isin(["Saturday", "Sunday"]).astype(int)
        # Scale and encode
        df[self.numerical_features] = self.scaler.transform(df[self.numerical_features])
        df[self.categorical_features] = self.encoder.transform(df[self.categorical_features])
        return df

    def fit_transform(self, df: pd.DataFrame):
        self.fit(df)
        return self.transform(df)