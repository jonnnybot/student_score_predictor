import joblib as jb
import pandas as pd
import numpy as np
import os
from flask import Flask, render_template, request, jsonify

current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(current_dir, 'models')
reg = jb.load(model_dir + '/linear_regression_model.joblib')

app = Flask(__name__, static_folder='../public', template_folder='../public')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    print(data)
    features = np.array([float(data['hoursStudied']), float(data['previousScores']), float(data['sleepHours']), float(data['papersPracticed'])])
    features = features.reshape(1, -1)
    prediction = reg.predict(features)
    print(prediction)
    if prediction[0] > 100:
        prediction[0] = 100
    if prediction[0] < 0:
        prediction[0] = 0
    return jsonify({
        'success': True,
        'prediction': prediction[0]
    })

if __name__ == '__main__':
    app.run(debug=True)



