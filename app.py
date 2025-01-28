from flask import Flask, request, jsonify, render_template
from src.utils.utils import load_obj, preprocess_text
import re

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model and preprocesser at app startup
model = load_obj(
    file_path=r'model\model.pkl'
)

preprocesser = load_obj(
    file_path=r'preprocesser\preprocess_text.pkl'
)

def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    return text

def predict_sentiment(text):
    processed_text = preprocess_text(text)
    vectorized_text = preprocesser.transform([processed_text]) 
    prediction = model.predict(vectorized_text)[0] 

    sentiment_map = {0: 'Negative', 1: 'Positive'} 
    return sentiment_map.get(prediction, 'Unknown')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_sentiment_api():
    try:
        review_text = request.form.get('review_text')

        if not review_text:
            return jsonify({"error": "Field 'review_text' is required."}), 400

        sentiment = predict_sentiment(review_text)
        return render_template('result.html', sentiment=sentiment)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
