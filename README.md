# Podcast Listening Time Prediction

A machine learning web application that predicts the expected listening time for a podcast episode based on its features such as genre, length, host/guest popularity, sentiment, and more.

---

## 🚀 Features

- **Data Preprocessing:** Cleans, transforms, and engineers features from raw podcast data.
- **Model Training:** Trains a deep learning regression model to predict listening time.
- **Reusable Preprocessing:** Uses a saved preprocessor for consistent feature engineering and scaling during prediction.
- **Web Interface:** User-friendly frontend built with HTML, CSS, and JavaScript.
- **API Endpoint:** `/predict` endpoint for programmatic access.
- **Logging & Error Handling:** Robust logging and error reporting.

---

## 🏗️ Project Structure

```
PodcastListeningTimePrediction/
│
├── app.py                  # Flask app entry point
├── main.py                 # Pipeline runner (training, evaluation)
├── src/
│   └── PodcastListeningTimePrediction/
│       ├── components/
│       │   ├── data_transformation.py
│       │   ├── model_trainer.py
│       │   ├── model_evaluation.py
│       │   └── preprocessor.py
│       ├── pipeline/
│       │   ├── data_ingestion_pipeline.py
│       │   ├── data_transformation_pipeline.py
│       │   ├── model_trainer_pipeline.py
│       │   ├── model_evaluation_pipeline.py
│       │   └── prediction_pipeline.py
│       ├── config/
│       │   └── configuration.py
│       └── ...
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── config/
│   └── config.yaml
├── schema.yaml
└── README.md
```

---

## 📦 Setup & Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/yourusername/PodcastListeningTimePrediction.git
    cd PodcastListeningTimePrediction
    ```

2. **Create and activate a virtual environment**
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On Mac/Linux
    ```

3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your data**
    - Place your dataset in the appropriate folder as specified in `config/config.yaml`.

---

## 🏃‍♂️ How to Run

### 1. **Train the Model**

```sh
python main.py
```
- This will run the full pipeline: data ingestion, transformation, model training, and evaluation.
- The trained model and preprocessor will be saved in the `artifacts/` directory.

### 2. **Start the Web App**

```sh
python app.py
```
- The app will be available at [http://localhost:5050/](http://localhost:5050/).

### 3. **Use the Web Interface**

- Fill in the podcast episode details in the form.
- Click "Predict" to see the predicted listening time.

---

## 🧩 Example Input Features

- Podcast Name
- Episode Title
- Episode Length (minutes)
- Genre
- Host Popularity (%)
- Publication Day
- Publication Time
- Guest Popularity (%)
- Number of Ads
- Episode Sentiment

---

## 📝 Notes

- Make sure to run the training pipeline before using the prediction endpoint.
- The preprocessor ensures that all feature engineering and scaling is consistent between training and prediction.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [TensorFlow/Keras](https://www.tensorflow.org/)
- [scikit-learn](https://scikit-learn.org/)
-