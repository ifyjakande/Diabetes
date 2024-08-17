import streamlit as st
import pickle
import joblib
import pandas as pd

st.title("Predictive Application for 30-Day Diabetes Readmission Risk")

st.text("An App Built by Ifeanyi Ejiofor")
st.text("Student ID: B00898539")
st.text("School of Computing, Engineering and Intelligent Systems, Magee Campus")
st.text("Supervisor: Girijesh Prasad")

st.write("This app uses 17 inputs to classify patients as readmitted or not readmitted using the model built on the diabetes dataset. Use the form below to get started!")

model = open("readmission_model.pickle", "rb")
diabetes = pickle.load(model)
model.close()


number_emergency = st.number_input("Number of emergency visits of the patient in the year preceding the encounter:", min_value = 0)
number_inpatient = st.number_input("Number of inpatient visits of the patient in the year preceding the encounter:", min_value = 0)
number_diagnoses = st.number_input("Number of diagnoses entered to the system:", min_value = 1)
race = st.selectbox("Race:",  options = ["Caucasian", "African American", "Hispanic", "Asian", "Others"])
gender = st.selectbox("Gender:",  options = ["Male", "Female"])
metformin = st.selectbox("Was metformin prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
repaglinide = st.selectbox("Was repaglinide prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
nateglinide = st.selectbox("Was nateglinide prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
chlorpropamide = st.selectbox("Was chlorpropamide prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
glimepiride = st.selectbox("Was glimepiride prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
acetohexamide =  st.selectbox("Was acetohexamide prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
glipizide = st.selectbox("Was glipizide prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
tolbutamide = st.selectbox("Was tolbutamide prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
pioglitazone = st.selectbox("Was pioglitazone prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
rosiglitazone = st.selectbox("Was rosiglitazone prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
acarbose = st.selectbox("Was acarbose prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
miglitol = st.selectbox("Was miglitol prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
troglitazone = st.selectbox("Was troglitazone prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
tolazamide = st.selectbox("Was tolazamide prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
insulin = st.selectbox("Was insulin prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
glyburide_metformin = st.selectbox("Was glyburide-metformin prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
glipizide_metformin = st.selectbox("Was glipizide-metformin prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
glimepiride_pioglitazone = st.selectbox("Was glimepiride-pioglitazone prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
metformin_rosiglitazone = st.selectbox("Was metformin-rosiglitazone prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
metformin_pioglitazone = st.selectbox("Was metformin-pioglitazone prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
change = st.selectbox("Was there a change in diabetic medications?:", options = ["No", "Yes"])
diabetesmed = st.selectbox("Was there any diabetic medication prescribed?:", options = ["No", "Yes"])


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

if st.button("Predict"):
    result = prediction[0]
    if result == 0:
        result = 'Not Readmitted'
    else:
        result = 'Readmitted'

    st.write("Patient Predicted to be {}".format(result))