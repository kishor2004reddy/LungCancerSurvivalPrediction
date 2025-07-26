from PodcastListeningTimePrediction import logger
from flask import Flask, request, render_template, jsonify
from PodcastListeningTimePrediction.pipeline.prediction_pipeline import PredictionPipeline
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        pipeline = PredictionPipeline()
        prediction = pipeline.predict(
            Podcast_Name=data['Podcast_Name'],
            Episode_Title=data['Episode_Title'],
            Episode_Length_minutes=float(data['Episode_Length_minutes']),
            Genre=data['Genre'],
            Host_Popularity_percentage=float(data['Host_Popularity_percentage']),
            Publication_Day=data['Publication_Day'],
            Publication_Time=data['Publication_Time'],
            Guest_Popularity_percentage=float(data['Guest_Popularity_percentage']),
            Number_of_Ads=int(data['Number_of_Ads']),
            Episode_Sentiment=data['Episode_Sentiment']
        )
        return jsonify({'prediction': prediction})
    except Exception as e:
        logger.exception(f"Prediction failed: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port)

