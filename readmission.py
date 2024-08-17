import streamlit as st
import pickle
import pandas as pd

# Set page config for a centered layout
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

# App title and subtitle with icon
st.markdown("<h1 class='main-title'><i class='fas fa-heartbeat'></i> Diabetes Readmission Risk Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Developed by Ifeanyi Ejiofor</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Student ID: B00898539</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>School of Computing, Engineering and Intelligent Systems, Magee Campus</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Supervisor: Girijesh Prasad</p>", unsafe_allow_html=True)

st.markdown("<p><i class='fas fa-info-circle'></i> This application predicts the 30-day readmission risk for diabetes patients based on various factors. Please fill in the form below with the patient's information to get a prediction.</p>", unsafe_allow_html=True)

# Load the model
def load_model():
    with open("readmission_model.pickle", "rb") as model_file:
        return pickle.load(model_file)

diabetes = load_model()

# Patient Information section with icon
st.markdown("<h3 class='icon-title'><i class='fas fa-user'></i> Patient Information</h3>", unsafe_allow_html=True)

number_emergency = st.number_input("Number of emergency visits in the past year:", min_value=0, value=1)
number_inpatient = st.number_input("Number of inpatient visits in the past year:", min_value=0, value=0)
number_diagnoses = st.number_input("Number of diagnoses entered to the system:", min_value=1, value=5)
race = st.selectbox("Race:", options=["Caucasian", "African American", "Hispanic", "Asian", "Others"], index=0)
gender = st.selectbox("Gender:", options=["Male", "Female"], index=0)

# Medication Information section with icon
st.markdown("<h3 class='icon-title'><i class='fas fa-pills'></i> Medication Information</h3>", unsafe_allow_html=True)

medication_options = ["No", "Up", "Down", "Steady"]
metformin = st.selectbox("Metformin prescription status:", options=medication_options, index=0)
repaglinide = st.selectbox("Repaglinide prescription status:", options=medication_options, index=0)
nateglinide = st.selectbox("Nateglinide prescription status:", options=medication_options, index=0)
chlorpropamide = st.selectbox("Chlorpropamide prescription status:", options=medication_options, index=0)
glimepiride = st.selectbox("Glimepiride prescription status:", options=medication_options, index=0)
acetohexamide = st.selectbox("Acetohexamide prescription status:", options=medication_options, index=0)
glipizide = st.selectbox("Glipizide prescription status:", options=medication_options, index=0)
tolbutamide = st.selectbox("Tolbutamide prescription status:", options=medication_options, index=0)
pioglitazone = st.selectbox("Pioglitazone prescription status:", options=medication_options, index=0)
rosiglitazone = st.selectbox("Rosiglitazone prescription status:", options=medication_options, index=0)
acarbose = st.selectbox("Acarbose prescription status:", options=medication_options, index=0)
miglitol = st.selectbox("Miglitol prescription status:", options=medication_options, index=0)
troglitazone = st.selectbox("Troglitazone prescription status:", options=medication_options, index=0)
tolazamide = st.selectbox("Tolazamide prescription status:", options=medication_options, index=0)
insulin = st.selectbox("Insulin prescription status:", options=medication_options, index=0)
glyburide_metformin = st.selectbox("Glyburide-metformin prescription status:", options=medication_options, index=0)
glipizide_metformin = st.selectbox("Glipizide-metformin prescription status:", options=medication_options, index=0)
glimepiride_pioglitazone = st.selectbox("Glimepiride-pioglitazone prescription status:", options=medication_options, index=0)
metformin_rosiglitazone = st.selectbox("Metformin-rosiglitazone prescription status:", options=medication_options, index=0)
metformin_pioglitazone = st.selectbox("Metformin-pioglitazone prescription status:", options=medication_options, index=0)
change = st.selectbox("Was there a change in diabetic medications?:", options=["No", "Yes"], index=0)
diabetesmed = st.selectbox("Was there any diabetic medication prescribed?:", options=["Yes", "No"], index=0)

# Data processing
race_africanamerican, race_asian, race_caucasian, race_hispanic, race_others = 0, 0, 0, 0, 0
if race == 'African American':
    race_africanamerican = 1
elif race == 'Asian':
    race_asian = 1
elif race == 'Caucasian':
    race_caucasian = 1
elif race == 'Hispanic':
    race_hispanic = 1
elif race == 'Others':
    race_others = 1

gender_female, gender_male = 0, 0
if gender == 'Male':
    gender_male = 1
elif gender == 'Female':
    gender_female = 1

def process_medication(med_status):
    return [1 if med_status == status else 0 for status in ["Up", "Down", "Steady", "No"]]

metformin_up, metformin_down, metformin_steady, metformin_no = process_medication(metformin)
repaglinide_up, repaglinide_down, repaglinide_steady, repaglinide_no = process_medication(repaglinide)
nateglinide_up, nateglinide_down, nateglinide_steady, nateglinide_no = process_medication(nateglinide)
chlorpropamide_up, chlorpropamide_down, chlorpropamide_steady, chlorpropamide_no = process_medication(chlorpropamide)
glimepiride_up, glimepiride_down, glimepiride_steady, glimepiride_no = process_medication(glimepiride)
acetohexamide_up, acetohexamide_down, acetohexamide_steady, acetohexamide_no = process_medication(acetohexamide)
glipizide_up, glipizide_down, glipizide_steady, glipizide_no = process_medication(glipizide)
tolbutamide_up, tolbutamide_down, tolbutamide_steady, tolbutamide_no = process_medication(tolbutamide)
pioglitazone_up, pioglitazone_down, pioglitazone_steady, pioglitazone_no = process_medication(pioglitazone)
rosiglitazone_up, rosiglitazone_down, rosiglitazone_steady, rosiglitazone_no = process_medication(rosiglitazone)
acarbose_up, acarbose_down, acarbose_steady, acarbose_no = process_medication(acarbose)
miglitol_up, miglitol_down, miglitol_steady, miglitol_no = process_medication(miglitol)
troglitazone_up, troglitazone_down, troglitazone_steady, troglitazone_no = process_medication(troglitazone)
tolazamide_up, tolazamide_down, tolazamide_steady, tolazamide_no = process_medication(tolazamide)
insulin_up, insulin_down, insulin_steady, insulin_no = process_medication(insulin)
glyburide_metformin_up, glyburide_metformin_down, glyburide_metformin_steady, glyburide_metformin_no = process_medication(glyburide_metformin)
glipizide_metformin_up, glipizide_metformin_down, glipizide_metformin_steady, glipizide_metformin_no = process_medication(glipizide_metformin)
glimepiride_pioglitazone_up, glimepiride_pioglitazone_down, glimepiride_pioglitazone_steady, glimepiride_pioglitazone_no = process_medication(glimepiride_pioglitazone)
metformin_rosiglitazone_up, metformin_rosiglitazone_down, metformin_rosiglitazone_steady, metformin_rosiglitazone_no = process_medication(metformin_rosiglitazone)
metformin_pioglitazone_up, metformin_pioglitazone_down, metformin_pioglitazone_steady, metformin_pioglitazone_no = process_medication(metformin_pioglitazone)

change_no, change_ch = (1, 0) if change == 'No' else (0, 1)
diabetesmed_no, diabetesmed_yes = (1, 0) if diabetesmed == 'No' else (0, 1)

my_predictors = {
    'number_emergency': number_emergency, 
    'number_inpatient': number_inpatient, 
    'number_diagnoses': number_diagnoses, 
    'race_others': race_others,
    'gender_female': gender_female,
    'metformin_steady': metformin_steady,
    'repaglinide_no': repaglinide_no,
    'nateglinide_no': nateglinide_no,
    'chlorpropamide_no': chlorpropamide_no,
    'glimepiride_steady': glimepiride_steady,
    'acetohexamide_no': acetohexamide_no,
    'glipizide_no': glipizide_no,
    'tolbutamide_no': tolbutamide_no,
    'pioglitazone_steady': pioglitazone_steady,
    'rosiglitazone_steady': rosiglitazone_steady,
    'acarbose_no': acarbose_no,
    'miglitol_no': miglitol_no,
    'troglitazone_no': troglitazone_no,
    'tolazamide_no': tolazamide_no,
    'insulin_down': insulin_down,
    'insulin_no': insulin_no,
    'insulin_steady': insulin_steady,
    'glyburide_metformin_no': glyburide_metformin_no,
    'glipizide_metformin_no': glipizide_metformin_no,
    'glimepiride_pioglitazone_no': glimepiride_pioglitazone_no,
    'metformin_rosiglitazone_no': metformin_rosiglitazone_no,
    'metformin_pioglitazone_no': metformin_pioglitazone_no,
    'change_ch': change_ch,
    'diabetesmed_no': diabetesmed_no,
    'diabetesmed_yes': diabetesmed_yes
}

df = pd.DataFrame.from_dict([my_predictors])

# Prediction button and result display
if st.button("Predict Readmission Risk", key="predict_button"):
    prediction = diabetes.predict(df)
    prediction_proba = diabetes.predict_proba(df)
    
    result = prediction[0]
    probability = prediction_proba[0][1]  # Probability of being readmitted
    
    if result == 0:
        st.markdown(f"""
        <div class='prediction-result not-readmitted'>
            <i class='fas fa-check-circle'></i> Patient Predicted: Not Readmitted
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class='prediction-result readmitted'>
            <i class='fas fa-exclamation-triangle'></i> Patient Predicted: Readmitted<br>
            Readmission Probability: {probability:.2%}
        </div>
        """, unsafe_allow_html=True)

# Footer with icon
st.markdown("---")
st.markdown("<p style='text-align: center; color: #7f8c8d;'><i class='far fa-copyright'></i> 2024 Diabetes Readmission Risk Predictor. All rights reserved.</p>", unsafe_allow_html=True)