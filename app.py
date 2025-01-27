from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Sentiment Analysis API!"

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    try:
        # Get the input JSON payload
        data = request.get_json()
        if 'text' not in data:
            return jsonify({'error': 'Please provide text for analysis.'}), 400

        text = data['text']
        
        # Perform sentiment analysis using TextBlob
        blob = TextBlob(text)
        sentiment = blob.sentiment

        response = {
            'text': text,
            'polarity': sentiment.polarity,  # Polarity ranges from -1 (negative) to 1 (positive)
            'subjectivity': sentiment.subjectivity  # Subjectivity ranges from 0 (objective) to 1 (subjective)
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
