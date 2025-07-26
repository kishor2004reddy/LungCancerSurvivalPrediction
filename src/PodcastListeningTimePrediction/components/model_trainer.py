from PodcastListeningTimePrediction import logger
from PodcastListeningTimePrediction.entity.config_entity import ModelTrainingConfig
import pandas as pd
import joblib
from PodcastListeningTimePrediction.components.preprocessor import PodcastPreprocessor

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping

class ModelTraining:

    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def train_model(self):

        train = pd.read_csv(self.config.train_data_path)
        test = pd.read_csv(self.config.test_data_path)

        # Fit preprocessor on training data and save
        preprocessor = PodcastPreprocessor()
        preprocessor.fit(train)
        joblib.dump(preprocessor, self.config.preprocessor_path)

        # Transform train and test data
        X_train = preprocessor.transform(train).drop(columns=[self.config.target_column])
        y_train = train[self.config.target_column]
        X_test = preprocessor.transform(test).drop(columns=[self.config.target_column])
        y_test = test[self.config.target_column]

        

        model = Sequential([
            Input(shape=(X_train.shape[1],)),
            Dense(256, activation='relu'),
            Dense(128, activation='relu'),
            Dense(64, activation='relu'),
            Dense(10, activation='relu'),
            Dropout(0.2),
            Dense(1)
        ])

        logger.info(f"Model Summary: {model.summary()}")

        # Compile the model
        optimizer = Adam(learning_rate = 0.05)

        model.compile(
            optimizer=optimizer,
            loss='mean_squared_error',
            metrics=['RootMeanSquaredError']
        )

        # Early stopping
        early_stop = EarlyStopping(monitor='val_loss', patience=30, restore_best_weights=True)

        # Train the model
        history = model.fit(
            X_train, y_train,
            batch_size = 256,
            validation_data=(X_test, y_test),
            epochs=100,
            callbacks=[early_stop],
            verbose=1
        )
        logger.info(f"Training History: {history.history}")
        model.save(self.config.model_path)




