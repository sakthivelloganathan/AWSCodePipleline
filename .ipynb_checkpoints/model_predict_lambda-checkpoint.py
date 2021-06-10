#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 21:06:35 2018

@author: vivekkalyanarangan
"""

import pickle
from flask import Flask, request, url_for, redirect, render_template, jsonify
from flasgger import Swagger
import numpy as np
import pandas as pd
import joblib

# from flask_restful import Api, Resource, reqparse

with open('C:/Users/rgayu/PycharmProjects/Salarydata.pkl', 'rb') as model_file:
    model = joblib.load(model_file)

app = Flask(__name__, template_folder='templates')
swagger = Swagger(app)


@app.route('/')
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_iriss():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: YearsExperience
        in: query
        type: number
        required: true
    responses:
        200:
            description: A list of colors (may be filtered by palette)
    """
    YearsExperience = request.args.get("YearsExperience")
    Salary = request.args.get("Salary")

    prediction = model.predict(np.array([[YearsExperience]]))
    print(prediction)
    result = str(prediction)
    return jsonify(result)
    #return render_template('index.html', pred='Expected Bill will be {}'.format(result))


if __name__ == '__main__':
    app.run(debug=True)