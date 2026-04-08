import streamlit as st
import joblib
import pandas as pd

import os

if not os.path.exists('placement-prediction_model.pkl'):
    st.error("Model file not found!")
else:
    model = joblib.load('placement-prediction_model.pkl')

st.set_page_config(page_title="Placement Prediction System", layout="centered")

st.title("🎓 Smart Placement Prediction System")
st.write("Enter Student Details")

# Form
with st.form("student_form"):

    age = st.number_input("Age", 17, 30)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    degree = st.selectbox("Degree", ["BCA", "BTech", "BSc", "MCA", "Other"])
    branch = st.selectbox("Branch",['ME','ECE','CSE' ,'IT' ,'Civil'])
    cgpa = st.slider("CGPA", 0.0, 10.0, 6.0)

    internships = st.number_input("Internships", 0, 10)
    projects = st.number_input("Projects", 0, 20)

    coding_skills = st.slider("Coding Skills", 1, 10)
    communication_skills = st.slider("Communication Skills", 1, 10)
    aptitude_score = st.slider("Aptitude Test Score", 0, 100)
    soft_skills = st.slider("Soft Skills Rating", 1, 10)

    certifications = st.number_input("Certifications", 0, 15)
    backlogs = st.number_input("Backlogs", 0, 20)

    submit = st.form_submit_button("Predict Placement")


if submit:
    if submit:

        data = pd.DataFrame({
            'Age':[age],
            'Gender':[gender],
            'Degree':[degree],
            'Branch':[branch],
            'CGPA':[cgpa],
            'Internships':[internships],
            'Projects':[projects],
            'Coding_Skills':[coding_skills],
            'Communication_Skills':[communication_skills],
            'Aptitude_Test_Score':[aptitude_score],
            'Soft_Skills_Rating':[soft_skills],
            'Certifications':[certifications],
            'Backlogs':[backlogs]
        })

        ans = model.predict(data)

        if ans[0] == 1:
            st.success("✅ Student is Likely to be Placed!")
        else:
            st.error("❌ Student is Not Likely to be Placed.")
