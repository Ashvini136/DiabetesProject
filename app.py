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
                         ['Diabetes_Prediction'])



#prediction page
if (selected=='Diabetes_Prediction'):
    st.title("Diabetes prediction using ML")

    Pregnancies=st.text_input(" Number of pregnancies")
    Glucose=st.text_input(" Glucose level in blood")
    BloodPressure=st.text_input(" Blood pressure")
    SkinThickness=st.text_input(" thickness of the skin")

    Insulin=st.text_input(" Insulin level in blood")
    BMI=st.text_input(" Body mass index")
    
    
    DiabetesPedigreeFunction=st.text_input(" Diabetes percentage")
    Age= st.text_input(" Enter the Age")

    
    
    
    L=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']

    prediction=""
    #creating button for prediction
    if st.button("Prediction"):
        Diabetes=model.predict([L])
        prediction=Diabetes[0]

    st.success(prediction)



if (selected=='Diamond Price Prediction'):
    st.title("Diamond Price Prediction using ML")


