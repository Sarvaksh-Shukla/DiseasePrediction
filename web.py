import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Prediction Of Disease Outbreak",layout='wide',page_icon='🧑‍⚕️')

diabetes_model=pickle.load(open(r"C:\Users\Sarvaksh\Documents\DiseasePrediction\saved_models\diabetes_model.sav",'rb'))
heart_model=pickle.load(open(r"C:\Users\Sarvaksh\Documents\DiseasePrediction\saved_models\heart_model.sav",'rb'))
parkinsons_model=pickle.load(open(r"C:\Users\Sarvaksh\Documents\DiseasePrediction\saved_models\parkinsons_model.sav",'rb'))

with st.sidebar:
    selected=option_menu('Prection od Disease Outbreak System',['Diabetes Prediction','Heart Prediction','Parkinsons Prediction'],
                         menu_icon='hospital-fill',icons=['activity','heart-fill','person-fill'],default_index=0)
    

if selected =='Diabetes Prediction':
    st.title('Diabetes Prediction')
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number Of pregnancies')
    with col2:
        Gulucose=st.text_input('Gulucose Level')
    with col3:
        Pressure=st.text_input('Blood Pressure')
    with col1:
        SkinThickness=st.text_input('Skin Thickness Input')
    with col2:
        Insulin=st.text_input('Insulin Level')
    with col3:
        bmi=st.text_input('BMI value')
    with col1:
        DiabetsPredigreeFunction=st.text_input('Diabetes Pedigree Function')
    with col2:
        Age=st.text_input('Age')
    diab_diagnosis ='Please give INPUT'
    if st.button('Diabetes Diagnosis RESULT'):
        user_input=[Pregnancies,Gulucose,SkinThickness,Pressure,Insulin,bmi,DiabetsPredigreeFunction,Age]
        user_input=[float(x) for x in user_input]
        diab_pred=diabetes_model.predict([user_input])
        if diab_pred[0]==1:
            diab_diagnosis='The person is diabetic'
        else:
            diab_diagnosis='The person is NOT diabetic'
    st.success(diab_diagnosis)
    