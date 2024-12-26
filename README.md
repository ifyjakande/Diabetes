# 🏥 Diabetes Readmission Risk Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://diabetes-pred.streamlit.app/)

## ⚠️ Educational Purpose Disclaimer
This project was developed for educational purposes only. It should not be used for making real medical decisions. Always consult with qualified healthcare professionals for medical advice.

## 🔍 Overview
A simple healthcare analytics solution that predicts hospital readmission risk for diabetes patients. Using machine learning, it analyzes patient data to predict 30-day readmission risk.

![Application Screenshot](diabetes-app.jpg)

## ✨ Features
- Patient Information Analysis
  - Patient demographics
  - Visit history data
  - Diagnosis information
  - Medication tracking
- Risk prediction with probability scores
- User-friendly healthcare interface

## 🛠️ Technology Stack
- Frontend: Streamlit
- ML Model: XGBoost
- Data Analysis: Pandas
- UI/UX: Custom CSS with Streamlit

## 💻 Local Development Setup
1. Clone the repository:
```bash
git clone https://github.com/ifyjakande/diabetes-readmission-predictor.git
cd diabetes-readmission-predictor
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

## 🤖 Model Information
The application uses an XGBoost model trained on historical diabetes patient data to predict readmission risk based on various patient factors.

## 📚 Dataset
This project uses the Diabetes 130-US hospitals for years 1999-2008 dataset from the UCI Machine Learning Repository. You can find the dataset here:
[UCI ML Repository - Diabetes Dataset](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008)

## 📋 Requirements
- Python 3.8+
- Streamlit
- Pandas
- XGBoost
- Pickle

## 🚀 Deployment
The application is deployed on Streamlit Cloud and can be accessed at [https://diabetes-pred.streamlit.app/](https://diabetes-pred.streamlit.app/)

To deploy your own instance:
1. Fork this repository
2. Connect your GitHub account to Streamlit Cloud
3. Deploy the application through Streamlit Cloud's interface

---
Made with ❤️ for improving diabetes patient care and education 🎓
