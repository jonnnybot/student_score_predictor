import joblib as jb
import pandas as pd
import numpy as np
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(current_dir, 'models')
print(current_dir)
print(model_dir)
reg = jb.load(model_dir + '/linear_regression_model.joblib')

X_test = {
    'Hours Studied': [5],
    'Previous Scores': [80],
    'Sleep Hours': [7.5],
    'Sample Question Papers Practiced': [3]
}
df = pd.DataFrame(X_test)
predictions = reg.predict(df)
print(predictions)

