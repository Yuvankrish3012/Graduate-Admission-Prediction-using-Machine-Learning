import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# 🎨 Streamlit page config
st.set_page_config(page_title="Graduate Admission Predictor 🎓", layout="wide", page_icon="📊")

# ✅ Load model and data with new cache decorators
@st.cache_resource
def load_model():
    return joblib.load("D:/ML PROJECTS/Graduate Admission Prediction using Machine Learning/admit_predictor_model.pkl")

@st.cache_data
def load_data():
    return pd.read_csv("D:/ML PROJECTS/Graduate Admission Prediction using Machine Learning/merged_admission_data.csv")

model = load_model()
df = load_data()

# 📊 Sidebar form for user input
st.sidebar.image("https://img.icons8.com/color/96/graduation-cap.png", use_container_width=True)
st.sidebar.title("🎓 Applicant Details")
with st.sidebar.form(key="input_form"):
    gre = st.slider("GRE Score", 260, 340, 320)
    toefl = st.slider("TOEFL Score", 80, 120, 110)
    univ_rating = st.selectbox("University Rating", [1, 2, 3, 4, 5])
    sop = st.slider("Statement of Purpose (SOP)", 1.0, 5.0, 3.5, 0.5)
    lor = st.slider("Letter of Recommendation (LOR)", 1.0, 5.0, 3.5, 0.5)
    cgpa = st.slider("Undergraduate CGPA", 6.0, 10.0, 8.5)
    research = st.radio("Research Experience", ["No", "Yes"])
    submit = st.form_submit_button("🔍 Predict Chance")

# 🔄 Preprocess input
research = 1 if research == "Yes" else 0
input_data = pd.DataFrame([{
    "GRE Score": gre,
    "TOEFL Score": toefl,
    "University Rating": univ_rating,
    "SOP": sop,
    "LOR": lor,
    "CGPA": cgpa,
    "Research": research
}])

# 🏛️ Logo and App title
st.markdown("""
    <div style='display: flex; align-items: center;'>
        <img src='https://img.icons8.com/color/96/graduation-cap.png' width='50' style='margin-right: 15px;' />
        <div>
            <h1 style='color: #3366cc; margin: 0;'>Graduate Admission Predictor 🎯</h1>
            <p style='font-size:18px; margin: 0;'>Estimate your admission chances into a university based on your academic profile</p>
        </div>
    </div>
    <hr>
""", unsafe_allow_html=True)

# 🔍 Predict and display result
if submit:
    prediction = model.predict(input_data)[0]
    percent = round(prediction * 100, 2)
    st.success(f"🎯 Your estimated **chance of admission** is: **{percent}%**")

    # 📉 Visualize result vs distribution
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df["Chance of Admit"], bins=20, color="skyblue", alpha=0.6)
    plt.axvline(prediction, color="crimson", linestyle="--", linewidth=3)
    plt.title("Your Score vs General Distribution", fontsize=14)
    plt.xlabel("Chance of Admit")
    st.pyplot(fig)

# 📊 Correlation heatmap
st.subheader("📌 Correlation Between Admission Factors")
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.heatmap(df.drop(columns=["Serial No."]).corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax2)
st.pyplot(fig2)

# 🧾 Sample data preview
st.subheader("📋 Sample of Merged Dataset")
st.dataframe(df.sample(10).reset_index(drop=True))

# 🧠 Footer
st.markdown("---")
st.markdown("<center>Built with ❤️ using Streamlit | © 2025</center>", unsafe_allow_html=True)
