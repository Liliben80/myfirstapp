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

# @app.route("/")
# def hello():
#     return "Hello World!"

# @app.route('/hello/<name>')
# def hello(name):
#     return 'Hello {}!'.format(name.capitalize())

# Prediction with identifier
@app.route('/<int:id_customer>', methods=["GET"])
def predict(id_customer):
    tab = data[data['SK_ID_CURR']==id_customer]
    result = {'Probability' : tab.iloc[0]['Probability'], 'Classe' : tab.iloc[0]['Prediction']}
    return jsonify(result)



# Excecution
if __name__ == "__main__":
    data = pickle.load(open('C:/Users/zahra/P7_Ben Ali_Linda/myfirstapp/df_modelisation.pkl', 'rb'))
    model = pickle.load(open('C:/Users/zahra/P7_Ben Ali_Linda/myfirstapp/model.pkl', 'rb'))
    thres_choice =  0.8
    app.run()