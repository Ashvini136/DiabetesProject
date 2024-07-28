import numpy as np
import pandas as pd
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import LabelEncoder
Le=LabelEncoder()


# loading the model
model=pickle.load(open("diabetes_rf.pkl","rb"))

# sidebar for navigator

with st.sidebar:
    selected=option_menu("Diabetes Predicting System",
                         ['Diabetes_Prediction',
                          'Heart_Prediction'])



#prediction page
if (selected=='Diabetes_Prediction'):
    st.title("Diabetes prediction using ML")

    col1,col2,col3=st.columns(3)

    with col1:

        Pregnancies=st.number_input(" Number of pregnancies",0,10)
        Glucose=st.number_input("Enter the Glucose level",0,200)
        BloodPressure=st.number_input(" Blood pressure",0,200)

    with col2:
        SkinThickness=st.number_input(" thickness of the skin",0,100)

        Insulin=st.number_input(" Insulin level in blood",0,300)
        BMI=st.number_input(" Body mass index",0,100)
    
    with col3:
        DiabetesPedigreeFunction=st.number_input(" Diabetes percentage",0,10)
        Age= st.number_input(" Enter the Age",0,100)


    L=[[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
       BMI, DiabetesPedigreeFunction, Age]]
    

    prediction=""
    #creating button for prediction
    if st.button("Prediction"):
        ans=model.predict(L)
        prediction=ans[0]
        #st.write(f'{"Patient has Diabetes" if prediction==1 else "Patient has No Diabetes"}')

        if prediction==1:
            st.write(" Patient has a Diabetes")
        else:
            st.write("Patient doesnot has as diabetes.")
    



    #st.button("Prediction")

if (selected=='Heart_Prediction'):
    st.title("Heart prediction using ML")





