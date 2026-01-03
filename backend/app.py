import joblib as jb
import pandas as pd
import numpy as np
import os
from flask import Flask, render_template, request, jsonify
import math

current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(current_dir, 'models')
linear_reg = jb.load(model_dir + '/linear_regression_model.joblib')
logistic_reg = jb.load(model_dir + '/logistic_regression_model.joblib')

app = Flask(__name__, static_folder='../public', template_folder='../public')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    print(data)
    features = np.array([float(data['hoursStudied']), float(data['previousScores']), float(data['extracurricularActivities']), float(data['sleepHours']), float(data['papersPracticed'])])
    features = features.reshape(1, -1)
    score_prediction = linear_reg.predict(features)
    pass_proba = logistic_reg.predict_proba(features)[:, 1]
    pass_proba_list = pass_proba.tolist()
    print(score_prediction)
    if score_prediction[0] > 100:
        score_prediction[0] = 100
    if score_prediction[0] < 0:
        score_prediction[0] = 0
    return jsonify({
        'success': True,
        'prediction': score_prediction[0],
        'pass_proba': round(float(pass_proba_list[0])*100, 5)
    })

if __name__ == '__main__':
    app.run(debug=True)



