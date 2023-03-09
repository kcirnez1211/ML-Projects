# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 18:45:51 2022

@author: HP
"""


import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('C:/Users/HP/OneDrive/Desktop/ML/Project ML/Deploying_ML_Model/trained_model.sav','rb'))

def diabetes_prediction(input_data):
    

    #converting to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshaping the data as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)



    prediction = loaded_model.predict(input_data_reshaped)

    if(prediction == 1):
      return'Diabetic'
    else:
      return'Non-Diabetic'
      
def main():
    #giving a title
    st.title('Diabetes Prediction Web App')
    
    #getting the input data from the user
    
    Pregnancies = st.text_input('No. of Pregnancies: ')
    Glucose = st.text_input('Glucose Level: ')
    BloodPressure = st.text_input('Blood Pressure Level: ')
    SkinThickness = st.text_input('Skin Thickness: ')
    Insulin = st.text_input('Insulin Level: ')
    BMI = st.text_input('BMI: ')
    DiabetesPedigreeFunction = st.text_input('DPF: ')
    Age = st.text_input('Age: ')

    #code for prediction
    diagnosis = ''

    #creating button for prediction
    if st.button('Diagnosis Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    st.success(diagnosis)

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    