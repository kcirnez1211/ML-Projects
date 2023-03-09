# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 13:27:33 2022

@author: HP
"""

import json
import requests

url = ' https://ml-model-api-heroku2.herokuapp.com/diabetes_prediction'

input_data_for_model = {
    'Pregnancies'  : 1,
    'Glucose' : 85,
    'BloodPressure'  :66,
    'SkinThickness' : 29,
    'Insulin' : 0,
    'BMI' :26.6,
    'DiabetesPedigreeFunction' :0.351,
    'Age' :31
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url,data=input_json)

print(response.text)