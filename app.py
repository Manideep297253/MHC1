app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    
    # preprocess message and create bag of words vector
    data = [message]
    vectorized_data = loaded_vectorizer.transform(data)
    
    # predict class (intent) of the message
    prediction = loaded_model.predict(vectorized_data)
    
    # map prediction to a human-readable intent name
    intent_name = None
    if prediction == 0:
        intent_name = 'greeting'
    elif prediction == 1:
        intent_name = 'farewell'
    elif prediction == 2:
        intent_name = 'affirmation'
    elif prediction == 3:
        intent_name = 'negation'
    elif prediction == 4:
        intent_name = 'unknown'
    
    # generate response based on the predicted intent
    response = 'I\'m sorry, but I can\'t answer that right now.'
    if intent_name ==
