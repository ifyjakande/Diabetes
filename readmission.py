import streamlit as st
import pickle
import pandas as pd

def load_model():
    with open("readmission_model.pickle", "rb") as model_file:
        return pickle.load(model_file)

def process_medication(med_status):
    return [int(med_status == status) for status in ["Up", "Down", "Steady", "No"]]

def main():
    st.set_page_config(layout="centered", page_title="Diabetes Readmission Risk Predictor")
    
    # Custom CSS for a more professional look with icon styling
    st.markdown("""
    <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');
        
        .reportview-container .main .block-container {
            max-width: 800px;
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }
        .main-title {
            font-size: 2rem;
            color: #FF0000;
            text-align: center;
            margin-bottom: 2rem;
        }
        .subtitle {
            font-size: 1rem;
            color: #34495e;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        .stButton>button {
            color: white;
            background-color: #3498db;
            border-radius: 5px;
            border: none;
            padding: 0.5rem 1rem;
            font-size: 1rem;
        }
        .stButton>button:hover {
            background-color: #2980b9;
        }
        .prediction-result {
            font-size: 1.5rem;
            font-weight: bold;
            text-align: center;
            margin-top: 2rem;
            padding: 1rem;
            border-radius: 5px;
        }
        .prediction-result.not-readmitted {
            background-color: #2ecc71;
            color: white;
        }
        .prediction-result.readmitted {
            background-color: #e74c3c;
            color: white;
        }
        .icon-title {
            font-size: 1.5rem;
            color: #2c3e50;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        .icon-title i {
            margin-right: 0.5rem;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='main-title'><i class='fas fa-heartbeat'></i> Diabetes Readmission Risk Predictor</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Developed by Ifeanyi Ejiofor</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Student ID: B00898539</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>School of Computing, Engineering and Intelligent Systems, Magee Campus</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Supervisor: Girijesh Prasad</p>", unsafe_allow_html=True)

    st.markdown("<p><i class='fas fa-info-circle'></i> This application predicts the 30-day readmission risk for diabetes patients based on various factors. Please fill in the form below with the patient's information to get a prediction.</p>", unsafe_allow_html=True)

    diabetes = load_model()

    st.markdown("<h3 class='icon-title'><i class='fas fa-user'></i> Patient Information</h3>", unsafe_allow_html=True)

    number_emergency = st.number_input("Number of emergency visits in the past year:", min_value=0, value=1)
    number_inpatient = st.number_input("Number of inpatient visits in the past year:", min_value=0, value=0)
    number_diagnoses = st.number_input("Number of diagnoses entered to the system:", min_value=1, value=5)
    race = st.selectbox("Race:", options=["Caucasian", "African American", "Hispanic", "Asian", "Others"], index=0)
    gender = st.selectbox("Gender:", options=["Male", "Female"], index=0)

    st.markdown("<h3 class='icon-title'><i class='fas fa-pills'></i> Medication Information</h3>", unsafe_allow_html=True)

    medication_options = ["No", "Up", "Down", "Steady"]
    medications = [
        "Metformin", "Repaglinide", "Nateglinide", "Chlorpropamide", "Glimepiride",
        "Acetohexamide", "Glipizide", "Tolbutamide", "Pioglitazone", "Rosiglitazone",
        "Acarbose", "Miglitol", "Troglitazone", "Tolazamide", "Insulin",
        "Glyburide-metformin", "Glipizide-metformin", "Glimepiride-pioglitazone",
        "Metformin-rosiglitazone", "Metformin-pioglitazone"
    ]

    medication_status = {med: st.selectbox(f"{med} prescription status:", options=medication_options, index=0) for med in medications}

    change = st.selectbox("Was there a change in diabetic medications?:", options=["No", "Yes"], index=0)
    diabetesmed = st.selectbox("Was there any diabetic medication prescribed?:", options=["Yes", "No"], index=0)

    # Data processing
    race_others = int(race == "Others")
    gender_female = int(gender == "Female")

    my_predictors = {
        'number_emergency': number_emergency, 
        'number_inpatient': number_inpatient, 
        'number_diagnoses': number_diagnoses, 
        'race_others': race_others,
        'gender_female': gender_female,
        'metformin_steady': int(medication_status["Metformin"] == "Steady"),
        'repaglinide_no': int(medication_status["Repaglinide"] == "No"),
        'nateglinide_no': int(medication_status["Nateglinide"] == "No"),
        'chlorpropamide_no': int(medication_status["Chlorpropamide"] == "No"),
        'glimepiride_steady': int(medication_status["Glimepiride"] == "Steady"),
        'acetohexamide_no': int(medication_status["Acetohexamide"] == "No"),
        'glipizide_no': int(medication_status["Glipizide"] == "No"),
        'tolbutamide_no': int(medication_status["Tolbutamide"] == "No"),
        'pioglitazone_steady': int(medication_status["Pioglitazone"] == "Steady"),
        'rosiglitazone_steady': int(medication_status["Rosiglitazone"] == "Steady"),
        'acarbose_no': int(medication_status["Acarbose"] == "No"),
        'miglitol_no': int(medication_status["Miglitol"] == "No"),
        'troglitazone_no': int(medication_status["Troglitazone"] == "No"),
        'tolazamide_no': int(medication_status["Tolazamide"] == "No"),
        'insulin_down': int(medication_status["Insulin"] == "Down"),
        'insulin_no': int(medication_status["Insulin"] == "No"),
        'insulin_steady': int(medication_status["Insulin"] == "Steady"),
        'glyburide_metformin_no': int(medication_status["Glyburide-metformin"] == "No"),
        'glipizide_metformin_no': int(medication_status["Glipizide-metformin"] == "No"),
        'glimepiride_pioglitazone_no': int(medication_status["Glimepiride-pioglitazone"] == "No"),
        'metformin_rosiglitazone_no': int(medication_status["Metformin-rosiglitazone"] == "No"),
        'metformin_pioglitazone_no': int(medication_status["Metformin-pioglitazone"] == "No"),
        'change_ch': int(change == "Yes"),
        'diabetesmed_no': int(diabetesmed == "No"),
        'diabetesmed_yes': int(diabetesmed == "Yes")
    }

    df = pd.DataFrame([my_predictors])

    if st.button("Predict Readmission Risk", key="predict_button"):
        prediction = diabetes.predict(df)
        prediction_proba = diabetes.predict_proba(df)
        
        result = prediction[0]
        probability = prediction_proba[0][1]
        
        result_class = "not-readmitted" if result == 0 else "readmitted"
        icon = "check-circle" if result == 0 else "exclamation-triangle"
        result_text = "Not Readmitted" if result == 0 else f"Readmitted<br>Readmission Probability: {probability:.2%}"
        
        st.markdown(f"""
        <div class='prediction-result {result_class}'>
            <i class='fas fa-{icon}'></i> Patient Predicted: {result_text}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #7f8c8d;'><i class='far fa-copyright'></i> 2024 Diabetes Readmission Risk Predictor. All rights reserved.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()