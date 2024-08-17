import streamlit as st
import pickle
import pandas as pd

# Set page config for a centered layout
st.set_page_config(layout="centered", page_title="Diabetes Readmission Risk Predictor")

# Custom CSS for a more professional look
st.markdown("""
<style>
    .reportview-container .main .block-container {
        max-width: 800px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .main-title {
        font-size: 2rem;
        color: #2c3e50;
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
</style>
""", unsafe_allow_html=True)

# App title and subtitle
st.markdown("<h1 class='main-title'>Diabetes Readmission Risk Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Developed by Ifeanyi Ejiofor</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Student ID: B00898539</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>School of Computing, Engineering and Intelligent Systems, Magee Campus</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Supervisor: Girijesh Prasad</p>", unsafe_allow_html=True)

st.write("This application predicts the 30-day readmission risk for diabetes patients based on various factors. Please fill in the form below with the patient's information to get a prediction.")

# Load the model
def load_model():
    with open("readmission_model.pickle", "rb") as model_file:
        return pickle.load(model_file)

diabetes = load_model()


# Updated input form with professional default values
number_emergency = st.number_input("Number of emergency visits in the past year:", min_value=0, value=1)
number_inpatient = st.number_input("Number of inpatient visits in the past year:", min_value=0, value=0)
number_diagnoses = st.number_input("Number of diagnoses entered to the system:", min_value=1, value=5)
race = st.selectbox("Race:", options=["Caucasian", "African American", "Hispanic", "Asian", "Others"], index=0)
gender = st.selectbox("Gender:", options=["Male", "Female"], index=0)

# Default most medications to "No" as it's likely the most common state
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


race_africanamerican, race_asian, race_caucasian, race_hispanic, race_others = 0, 0, 0, 0, 0
if race == 'African American':
    race_africanamerican = 1
elif race == 'Asian':
    race_asian = 1
elif race == 'Caucasian':
    race_caucasian = 1
elif race == 'Hispanic':
    race_hispanic = 1
elif race == 'Asian':
    race_asian = 1
elif race == 'Others':
    race_others = 1


gender_female, gender_male = 0, 0
if gender == 'Male':
    gender_male = 1
elif gender == 'Female':
    gender_female = 1

metformin_up, metformin_down, metformin_steady, metformin_no = 0, 0, 0, 0
if metformin == 'Up':
    metformin_up = 1
elif metformin == 'Down':
    metformin_down = 1
elif metformin == "Steady":
    metformin_steady = 1
elif metformin == "No":
    metformin_no = 1


repaglinide_up, repaglinide_down, repaglinide_steady, repaglinide_no = 0, 0, 0, 0
if repaglinide == 'Up':
    repaglinide_up = 1
elif repaglinide == 'Down':
    repaglinide_down = 1
elif repaglinide == "Steady":
    repaglinide_steady = 1
elif repaglinide == "No":
    repaglinide_no = 1


nateglinide_up, nateglinide_down, nateglinide_steady, nateglinide_no = 0, 0, 0, 0
if nateglinide == 'Up':
    nateglinide_up = 1
elif nateglinide == 'Down':
    nateglinide_down = 1
elif nateglinide == "Steady":
    nateglinide_steady = 1
elif nateglinide == "No":
    nateglinide_no = 1


chlorpropamide_up, chlorpropamide_down, chlorpropamide_steady, chlorpropamide_no = 0, 0, 0, 0
if chlorpropamide == 'Up':
    chlorpropamide_up = 1
elif chlorpropamide == 'Down':
    chlorpropamide_down = 1
elif chlorpropamide == "Steady":
    chlorpropamide_steady = 1
elif chlorpropamide == "No":
    chlorpropamide_no = 1


glimepiride_up, glimepiride_down, glimepiride_steady, glimepiride_no = 0, 0, 0, 0
if glimepiride == 'Up':
    glimepiride_up = 1
elif glimepiride == 'Down':
    glimepiride_down = 1
elif glimepiride == "Steady":
    glimepiride_steady = 1
elif glimepiride == "No":
    glimepiride_no = 1



acetohexamide_up, acetohexamide_down, acetohexamide_steady, acetohexamide_no = 0, 0, 0, 0
if acetohexamide == 'Up':
    acetohexamide_up = 1
elif acetohexamide == 'Down':
    acetohexamide_down = 1
elif acetohexamide == "Steady":
    acetohexamide_steady = 1
elif acetohexamide == "No":
    acetohexamide_no = 1


glipizide_up, glipizide_down, glipizide_steady, glipizide_no = 0, 0, 0, 0
if glipizide == 'Up':
    glipizide_up = 1
elif glipizide == 'Down':
    glipizide_down = 1
elif glipizide == "Steady":
    glipizide_steady = 1
elif glipizide == "No":
    glipizide_no = 1


tolbutamide_up, tolbutamide_down, tolbutamide_steady, tolbutamide_no = 0, 0, 0, 0
if tolbutamide == 'Up':
    tolbutamide_up = 1
elif tolbutamide == 'Down':
    tolbutamide_down = 1
elif tolbutamide == "Steady":
    tolbutamide_steady = 1
elif tolbutamide == "No":
    tolbutamide_no = 1


pioglitazone_up, pioglitazone_down, pioglitazone_steady, pioglitazone_no = 0, 0, 0, 0
if pioglitazone == 'Up':
    pioglitazone_up = 1
elif pioglitazone == 'Down':
    pioglitazone_down = 1
elif pioglitazone == "Steady":
    pioglitazone_steady = 1
elif pioglitazone == "No":
    pioglitazone_no = 1


rosiglitazone_up, rosiglitazone_down, rosiglitazone_steady, rosiglitazone_no = 0, 0, 0, 0
if rosiglitazone == 'Up':
    rosiglitazone_up = 1
elif rosiglitazone == 'Down':
    rosiglitazone_down = 1
elif rosiglitazone == "Steady":
    rosiglitazone_steady = 1
elif rosiglitazone == "No":
    rosiglitazone_no = 1


acarbose_up, acarbose_down, acarbose_steady, acarbose_no = 0, 0, 0, 0
if acarbose == 'Up':
    acarbose_up = 1
elif acarbose == 'Down':
    acarbose_down = 1
elif acarbose == "Steady":
    acarbose_steady = 1
elif acarbose == "No":
    acarbose_no = 1

miglitol_up, miglitol_down, miglitol_steady, miglitol_no = 0, 0, 0, 0
if miglitol == 'Up':
    miglitol_up = 1
elif miglitol == 'Down':
    miglitol_down = 1
elif miglitol == "Steady":
    miglitol_steady = 1
elif miglitol == "No":
    miglitol_no = 1

troglitazone_up, troglitazone_down, troglitazone_steady, troglitazone_no = 0, 0, 0, 0
if troglitazone == 'Up':
    troglitazone_up = 1
elif troglitazone == 'Down':
    troglitazone_down = 1
elif troglitazone == "Steady":
    troglitazone_steady = 1
elif troglitazone == "No":
    troglitazone_no = 1


tolazamide_up, tolazamide_down, tolazamide_steady, tolazamide_no = 0, 0, 0, 0
if tolazamide == 'Up':
    tolazamide_up = 1
elif tolazamide == 'Down':
    tolazamide_down = 1
elif tolazamide == "Steady":
    tolazamide_steady = 1
elif tolazamide == "No":
    tolazamide_no = 1


insulin_up, insulin_down, insulin_steady, insulin_no = 0, 0, 0, 0
if insulin == 'Up':
    insulin_up = 1
elif insulin == 'Down':
    insulin_down = 1
elif insulin == "Steady":
    insulin_steady = 1
elif insulin == "No":
    insulin_no = 1


glyburide_metformin_up, glyburide_metformin_down, glyburide_metformin_steady, glyburide_metformin_no = 0, 0, 0, 0
if glyburide_metformin == 'Up':
    glyburide_metformin_up = 1
elif glyburide_metformin == 'Down':
    glyburide_metformin_down = 1
elif glyburide_metformin == "Steady":
    glyburide_metformin_steady = 1
elif glyburide_metformin == "No":
    glyburide_metformin_no = 1


glipizide_metformin_up, glipizide_metformin_down, glipizide_metformin_steady, glipizide_metformin_no = 0, 0, 0, 0
if glipizide_metformin == 'Up':
    glipizide_metformin_up = 1
elif glipizide_metformin == 'Down':
    glipizide_metformin_down = 1
elif glipizide_metformin == "Steady":
    glipizide_metformin_steady = 1
elif glipizide_metformin == "No":
    glipizide_metformin_no = 1


glimepiride_pioglitazone_up, glimepiride_pioglitazone_down, glimepiride_pioglitazone_steady, glimepiride_pioglitazone_no = 0, 0, 0, 0
if glimepiride_pioglitazone == 'Up':
    glimepiride_pioglitazone_up = 1
elif glimepiride_pioglitazone == 'Down':
    glimepiride_pioglitazone_down = 1
elif glimepiride_pioglitazone == "Steady":
    glimepiride_pioglitazone_steady = 1
elif glimepiride_pioglitazone == "No":
    glimepiride_pioglitazone_no = 1



metformin_rosiglitazone_up, metformin_rosiglitazone_down, metformin_rosiglitazone_steady,  metformin_rosiglitazone_no = 0, 0, 0, 0
if metformin_rosiglitazone == 'Up':
    metformin_rosiglitazone_up = 1
elif metformin_rosiglitazone == 'Down':
    metformin_rosiglitazone_down = 1
elif metformin_rosiglitazone == "Steady":
    metformin_rosiglitazone_steady = 1
elif metformin_rosiglitazone == "No":
    metformin_rosiglitazone_no = 1


metformin_pioglitazone_up, metformin_pioglitazone_down, metformin_pioglitazone_steady,  metformin_pioglitazone_no = 0, 0, 0, 0
if metformin_pioglitazone == 'Up':
    metformin_pioglitazone_up = 1
elif metformin_pioglitazone == 'Down':
    metformin_pioglitazone_down = 1
elif metformin_pioglitazone == "Steady":
    metformin_pioglitazone_steady = 1
elif metformin_pioglitazone == "No":
    metformin_pioglitazone_no = 1


change_no, change_ch = 0, 0
if change == 'No':
    change_no = 1
elif change  == 'Yes':
    change_ch = 1


diabetesmed_no, diabetesmed_yes = 0, 0
if diabetesmed == 'No':
    diabetesmed_no = 1
elif diabetesmed  == 'Yes':
    diabetesmed_yes = 1

    
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
    'tolazamide_no':tolazamide_no,
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


prediction = diabetes.predict(df)

# Prediction button and result display
if st.button("Predict Readmission Risk", key="predict_button"):
    # Get prediction and probability
    prediction = diabetes.predict(df)
    prediction_proba = diabetes.predict_proba(df)
    
    result = prediction[0]
    probability = prediction_proba[0][1]  # Probability of being readmitted
    
    if result == 0:
        st.markdown(f"""
        <div class='prediction-result not-readmitted'>
            Patient Predicted: Not Readmitted
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class='prediction-result readmitted'>
            Patient Predicted: Readmitted<br>
            Readmission Probability: {probability:.2%}
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #7f8c8d;'>© 2024 Diabetes Readmission Risk Predictor. All rights reserved.</p>", unsafe_allow_html=True)