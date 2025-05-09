from flask import Flask, render_template, request, redirect, url_for, jsonify
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon')

app = Flask(__name__)

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return render_template('code.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    if email == "ghanashree2005@gmail.com" and password == "123456":
        return redirect(url_for('dashboard'))
    else:
        return "Invalid email or password. <a href='/'>Try again</a>"

@app.route('/dashboard')
def dashboard():
    return render_template('dash.html')

@app.route('/mood')
def mood():
    return render_template('mood.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json['text']
    sentiment_scores = analyzer.polarity_scores(text)
    compound = sentiment_scores['compound']

    if compound >= 0.5:
        mood = "Happy"
    elif compound >= 0.1:
        mood = "Neutral"
    elif compound > -0.3:
        mood = "Sad"
    elif compound > -0.6:
        mood = "Anxious"
    else:
        mood = "Depressed"

    suggestions = {
        "Happy": "Great job! Keep maintaining a healthy lifestyle and staying positive.",
        "Neutral": "Try doing things that bring you joy—like hobbies, music, or a walk in nature.",
        "Sad": "Consider talking to a friend, journaling, or taking time to rest and relax.",
        "Anxious": "Take deep breaths, practice mindfulness, or try light physical activity.",
        "Depressed": "It might help to speak with a mental health professional. You're not alone."
    }

    return jsonify({
        'sentiment': mood,
        'suggestion': suggestions[mood],
        'scores': sentiment_scores
    })

@app.route('/meditation')
def meditation():
    return render_template('meditation.html')

@app.route('/ai-suggest')
def ai_suggest():
    return render_template('ai_suggest.html')

@app.route('/therapist')
def therapist():
    return render_template('therapist.html')

if __name__ == '__main__':
    app.run(debug=True)
