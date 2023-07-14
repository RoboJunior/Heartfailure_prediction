import pickle
import streamlit as st

st.set_page_config(page_title="Heart-failure-prediction",page_icon="🫀",layout='wide')

st.header("Heart Failure prediction using Logistic Regression Model 🫀")


#loading the dataset using pickle
loaded_model = pickle.load(open('final_model.sav','rb'))

col1,col2 = st.columns(2)

with col1:
    age = st.slider("Enter your age ",28,77,30)
    st.success(f"Age {age} is selected")
    result = loaded_model.predict([[1,2,3,4,5,6,7,8,9,10,11]])
    sex = st.selectbox("Choose your Gender",[0,1])
    if sex==0:
        st.success("Gender female is selected")
    else:
        st.success("Gender male is selected")
    chest_pain_type = st.selectbox("Choose what type of chest pain you have",[0,1,2,3])
    if chest_pain_type == 0:
        st.success("Chest pain type ASY is selected")
    elif chest_pain_type == 1:
        st.success("Chest pain type ATA is selected")
    elif chest_pain_type == 2:
        st.success("Chest pain type NAP is selected")
    else:
        st.success("Chest pain type TA is selected")
    resting_bp = st.slider("Enter your restingbp",80,185,100)
    st.success(f"Resting bp {resting_bp} is selected")
    Cholesterol = st.slider("Enter your Cholesterol count",0,518,0)
    st.success(f"Cholesterol {Cholesterol} is selected")
    FastingBS = st.selectbox("Enter your FastingBS",[0,1])
    st.success(f"FastingBS {FastingBS} is selected")
with col2:
    restingecg = st.selectbox("Enter your restingecg",[0,1,2])
    if restingecg == 0:
        st.success("RestingECG LVH is selected")
    elif restingecg == 1:
        st.success("RestingECG Normal is selected")
    else:
        st.success("RestingECG ST is selected")
    maxhr = st.slider("Enter your MaxHR ",63,202,65)
    st.success(f"MaxHR {maxhr} is selected")
    exerciseangina = st.selectbox("Enter your ExerciseAngina ",[0,1])
    if exerciseangina == 0:
        st.success("ExerciseAngina No is selected")
    else:
        st.success("ExerciseAngina Yes is selected")
    oldpeak = st.slider("Enter your Oldpeak",-2,4,1)
    st.success(f"Oldpeak {oldpeak} is selected")
    st_slope = st.selectbox("Enter your STslope",[0,1,2])
    if st_slope == 0:
        st.success("STslope down is selected")
    elif st_slope == 1:
        st.success("STslope flat is selected")
    else:
        st.success("STslope up is selected")

    predicter = st.button("Start Predicting")
    if predicter:
        result = loaded_model.predict([[age,sex,chest_pain_type,resting_bp,Cholesterol,FastingBS,restingecg,maxhr,exerciseangina,oldpeak,st_slope]])
        if result == 0:
            st.success("Looks like you have no chance of heartfailure problem 🎉")
        else:
            st.error("Looks like you have chances of heartfailure 😔")
        
