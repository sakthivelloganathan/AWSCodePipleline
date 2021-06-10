#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 21:06:35 2018

@author: vivekkalyanarangan
"""

import pickle
from flask import Flask,request, url_for, redirect, render_template, jsonify
from flasgger import Swagger
import numpy as np
import pandas as pd
import joblib
#from flask_restful import Api, Resource, reqparse

with open('model/Salarydata.pkl', 'rb') as model_file:
    model = joblib.load(model_file)


app = Flask(__name__,template_folder='templates')
swagger = Swagger(app)

@app.route('/')
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_iris():
    int_features = [x for x in request.form.values()]
    s_length = int_features[0]
    s_width = int_features[1]
    p_length = int_features[2]
    p_width = int_features[3]
    print(s_length)
    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))
    print('prediction',prediction)
    result=str(prediction)
    #return jsonify(result)
    return render_template('index.html',prediction_text="Quality of Alcohol is {}".format(result))

# @app.route('/predict_file', methods=["POST"])
# def predict_iris_file():
#     """Example file endpoint returning a prediction of iris
#     ---
#     parameters:
#       - name: input_file
#         in: formData
#         type: file
#         required: true
#     """
#     input_data = pd.read_csv(request.files.get("input_file"), header=None)
#     prediction = model.predict(input_data)
#     return str(list(prediction))
def predict_iriss():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: true
      - name: s_width
        in: query
        type: number
        required: true
      - name: p_length
        in: query
        type: number
        required: true
      - name: p_width
        in: query
        type: number
        required: true
    responses:
        200:
            description: A list of colors (may be filtered by palette)
    """
    s_length = request.args.get("s_length")
    s_width = request.args.get("s_width")
    p_length = request.args.get("p_length")
    p_width = request.args.get("p_width")

    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))
    print(prediction)
    result=str(prediction)
    #return jsonify(result)
    return render_template('index.html',pred='Expected Bill will be {}'.format(result))
if __name__ == '__main__':
    app.run(debug=True)