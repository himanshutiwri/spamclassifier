from flask import Flask, render_template, request
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle
import string
import os

app = Flask(__name__)

# Ensure NLTK data is downloaded
nltk_data_dir = os.path.join(os.path.dirname(__file__), "nltk_data")
if not os.path.exists(nltk_data_dir):
    os.mkdir(nltk_data_dir)

nltk.data.path.append(nltk_data_dir)
nltk.download('punkt', download_dir=nltk_data_dir)
nltk.download('stopwords', download_dir=nltk_data_dir)

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))  # load once

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = [i for i in text if i.isalnum()]
    text = [i for i in y if i not in stop_words and i not in string.punctuation]
    text = [ps.stem(i) for i in text]

    return " ".join(text)

def predict_spam(message):
    # Preprocess
    transformed_sms = transform_text(message)
    # Vectorize
    vector_input = tfidf.transform([transformed_sms])
    # Predict
    result = model.predict(vector_input)[0]
    return result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_sms = request.form['message']
    result = predict_spam(input_sms)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
