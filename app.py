# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request
import json
import requests

# Numpy and pandas for data manipulation
import numpy as np
import pandas as pd 
import pickle

# Sklearn modelisation
import sklearn
import lightgbm
from lightgbm import LGBMClassifier

# Statement  
app = Flask(__name__)

data = pickle.load(open('df_modelisation.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
thres_choice = 0.8

# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route('/hello/<name>')
# def hello(name):
#     return 'Hello {}!'.format(name.capitalize())

# Prediction with identifier
@app.route('/predict/<int:id_customer>', methods=["GET"])
def predict(id_customer):
    tab = data[data['SK_ID_CURR']==id_customer]
    result = {'Probability' : tab.iloc[0]['Probability'], 'Classe' : tab.iloc[0]['Prediction']}
    return jsonify(result)

# Prediction by model
@app.route('/predict_model', methods=["POST", "GET"])
def predict_model():
    vector = request.get_json().get('vector')
    vector = np.array(vector)
    vector = vector.reshape(1,len(vector))
    proba = model.predict_proba(vector)[0][0]
    predict = 1 if proba > thres_choice else 0
    result = {'Probability' : proba, 'Classe' : predict}
    return jsonify(result)

# Excecution
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)