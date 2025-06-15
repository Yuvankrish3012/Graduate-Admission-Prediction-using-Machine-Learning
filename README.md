# Graduate-Admission-Prediction-using-Machine-Learning

This project predicts a student’s chance of admission to a graduate program based on academic metrics such as GRE scores, TOEFL scores, CGPA, and research experience. It includes an elegant Streamlit-based web application.

---

## 📁 Dataset

We used two datasets:
- `Admission_Predict.csv`
- `Admission_Predict_Ver1.1.csv`

These were merged into a single dataset of **900 rows** and 9 columns.  
Source: [Kaggle - Graduate Admission Dataset](https://www.kaggle.com/datasets/mohansacharya/graduate-admissions)

### 📌 Features:

| Feature              | Description                                           |
|----------------------|-------------------------------------------------------|
| GRE Score            | Graduate Record Examination score (out of 340)       |
| TOEFL Score          | TOEFL score (out of 120)                              |
| University Rating    | Rating of university (1 to 5)                         |
| SOP                  | Statement of Purpose strength (1.0 to 5.0)            |
| LOR                  | Letter of Recommendation strength (1.0 to 5.0)        |
| CGPA                 | Undergraduate GPA (out of 10)                         |
| Research             | Research experience (1 = Yes, 0 = No)                |
| Chance of Admit      | Admission probability (0.0 to 1.0)                    |

---

## 🧪 Model Training

We used a **Linear Regression model** to predict the admission chances:

- 🔁 Dataset split: `80%` training, `20%` testing
- 📈 Metrics used:
  - **MAE (Mean Absolute Error)**: `1.11`
  - **RMSE (Root Mean Squared Error)**: `1.87`
  - **R² Score**: `0.83`
  - 
## Visualizations 
📊 Exploratory Data Analysis
📉 Correlation heatmap
🔍 Distribution of Admission Chances

🖼️ Sample Visual Output:

![image](https://github.com/user-attachments/assets/5b069cb5-4ec6-441b-b22c-a1a2e58b2b11)
![image](https://github.com/user-attachments/assets/776bbe1c-4709-4b30-9a9e-9fa63fce974e)
![image](https://github.com/user-attachments/assets/39d05fed-9a78-4390-a5e3-1d83a05f621f)
![image](https://github.com/user-attachments/assets/a76e52d4-1dbb-41b2-9276-cf232cdc36ae)


## 💻 Streamlit Frontend
The frontend was built using Streamlit and includes:

🔷 Features:
🎓 Sidebar form for GRE, TOEFL, SOP, CGPA, etc.

🎯 Real-time prediction output with probability

📊 Histogram visualization of your prediction

🧾 Data sample preview

🌐 Clean UI with icon logo and styled title

## 📦 Streamlit Enhancements:
Logo added to the top-left header

Fixed deprecated methods:

st.cache ➝ st.cache_resource / st.cache_data

use_column_width ➝ use_container_width

Responsive layout with clean markdown and visuals

## 🚀 Run the Application
Make sure you've installed dependencies first:

bash
Copy
Edit
pip install -r requirements.txt
Then run the app with this one-liner:

bash
Copy
Edit
streamlit run "D:/ML PROJECTS/Graduate Admission Prediction using Machine Learning/admission_app.py"
📂 Project Structure
nginx
Copy
Edit
Graduate Admission Prediction/
│
├── admission_app.py                   # Streamlit frontend
├── admit_predictor_model.pkl          # Trained model
├── merged_admission_data.csv          # Merged dataset (900 rows)
├── Admission_Predict.csv              # Original dataset
├── Admission_Predict_Ver1.1.csv       # Additional dataset
├── README.md                          # Project documentation
└── requirements.txt                   # Required libraries
## 📌 Future Improvements
Add support for classification (accept/reject)

Integrate with a NoSQL DB to track user queries

Allow resume parsing and prediction from uploaded PDF

# 👨‍💻 Author
Yuvan Krishnan
Made with ❤️ for learning and real-world application
🔗 LinkedIn | GitHub | Portfolio

