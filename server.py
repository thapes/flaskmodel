import numpy as np
from flask import Flask, request, jsonify
import pickle


app = Flask(__name__)
# Load the model
model = pickle.load(open('model.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request and Make prediction using model loaded from disk as per the data.
    data = request.get_json(force=True)
    prediction = model.predict([[np.array(data['exp'])]])
    output = prediction[0] # Take the first value of prediction

    return jsonify(output)

if __name__ == '__main__':
    app.run(port=8080, debug=True)