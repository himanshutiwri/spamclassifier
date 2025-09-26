from flask import Flask, render_template, request
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle
import string
import os

app = Flask(__name__)

# =========================
# NLTK Setup
# =========================
nltk_data_dir = os.path.join(os.path.dirname(__file__), "nltk_data")
if not os.path.exists(nltk_data_dir):
    os.mkdir(nltk_data_dir)

# Add custom nltk data path
nltk.data.path.append(nltk_data_dir)

# Download required packages (only if missing)
nltk.download('punkt', download_dir=nltk_data_dir)
nltk.download('punkt_tab', download_dir=nltk_data_dir)
nltk.download('stopwords', download_dir=nltk_data_dir)

# Initialize Stemmer and Stopwords
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

# =========================
# Text preprocessing
# =========================
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    # Remove non-alphanumeric
    text = [i for i in text if i.isalnum()]
    # Remove stopwords & punctuation
    text = [i for i in text if i not in stop_words and i not in string.punctuation]
    # Stemming
    text = [ps.stem(i) for i in text]
    return " ".join(text)

# =========================
# Prediction function
# =========================
def predict_spam(message):
    transformed_sms = transform_text(message)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]
    return result

# =========================
# Routes
# =========================
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_sms = request.form['message']
    result = predict_spam(input_sms)
    return render_template('index.html', result=result)

# =========================
# Main
# =========================
if __name__ == '__main__':
    # Load model and vectorizer
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
    
    # Use PORT from Render or default 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

