from flask import Flask, render_template, request
import nltk
import os
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle
import string

app = Flask(__name__)

# Download NLTK data
nltk.download('punkt_tab')
nltk.download('stopwords')

# Initialize stemmer
ps = PorterStemmer()

# Text preprocessing function
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    # Remove non-alphanumeric
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    # Remove stopwords and punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()

    # Stemming
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Prediction function
def predict_spam(message):
    # Preprocess
    transformed_sms = transform_text(message)
    # Vectorize
    vector_input = tfidf.transform([transformed_sms])
    # Predict
    result = model.predict(vector_input)[0]
    return result

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_sms = request.form['message']
        result = predict_spam(input_sms)
        return render_template('index.html', result=result)  # Pass result to template

# Main
if __name__ == '__main__':
    # Load model and vectorizer
    tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))

    app.run(host='0.0.0.0', port=5000, debug=True)




