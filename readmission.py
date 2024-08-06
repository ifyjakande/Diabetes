import streamlit as st
import pickle
import pandas as pd

st.title("Predictive Application for 30-Day Diabetes Readmission Risk")

st.text("An App Built by Ifeanyi Ejiofor")
st.text("Student ID: B00898539")
st.text("School of Computing, Engineering and Intelligent Systems, Magee Campus")
st.text("Supervisor: Girijesh Prasad")

st.write("This app uses 17 inputs to classify patients as readmitted or not readmitted using the model built on the diabetes dataset. Use the form below to get started!")

model = open("readmission_model.pickle", "rb")
readd = pickle.load(model)
model.close()

selected_admission_type = st.selectbox("Admission type:", options = ["Emergency", "Urgent", "Elective", "Newborn", "Routine", " Pre-scheduled", "Transfer", "Not Available"])
discharge_deposition_id = st.selectbox("Discharge disposition:", options = ["Discharged to Home", "Expired", "Transferred to Another Facility", "Discharged to Rehabilitation", "Discharged to Nursing Home", "Discharged to Hospice", "Discharged to Home with Home Health Services", "Discharged Against Medical Advice", "Discharged to Assisted Living Facility", "Discharged to Long-Term Acute Care Hospital", "Discharged to Palliative Care", "Discharged to Family Care", "Discharged to Group Home", "Discharged to Substance Abuse Treatment Facility", "Discharged to Mental Health Facility", "Discharged to Dental Facility", "Discharged to Special Care Unit", "Discharged to Pediatric Facility", "Discharged to Adult Day Care", "Discharged to Mobile Health Services", "Discharged to Correctional Facility", "Discharged to Emergency Shelter", "Discharged to Home with Private Duty Nursing", "Discharged to Primary Care Physician", "Discharged to Clinical Trial", "Not Available"])
admission_source_id = st.selectbox("Admission source:",  options = ["Emergency Room", "Physician Referral", "Transfer from Another Hospital", "Direct Admission", "Urgent Care Center", "Outpatient Clinic", "Home Health Agency", "Long-Term Care Facility", "Palliative Care Provider", "Rehabilitation Facility", "Specialty Care Center", "Walk-In Clinic", "Laboratory", "Dental Office", "Mental Health Facility", "Substance Abuse Treatment Facility", "Not Available"])
time_in_hospital = st.number_input("Number of days between admission and discharge:",  min_value = 1)
num_procedures = st.number_input("Number of procedures (other than lab tests) performed during the encounter:",  min_value = 0)
num_medications = st.number_input("Number of distinct generic names administered during the encounter:",  min_value= 0)
number_outpatient = st.number_input("Number of outpatient visits of the patient in the year preceding the encounter:", min_value = 0)
number_emergency = st.number_input("Number of emergency visits of the patient in the year preceding the encounter:", min_value = 0)
number_inpatient = st.number_input("Number of inpatient visits of the patient in the year preceding the encounter:", min_value = 0)
number_diagnoses = st.number_input("Number of diagnoses entered to the system:", min_value = 1)
age = st.number_input("Age:", min_value = 5)
race = st.selectbox("Race:",  options = ["Caucasian", "African American", "Hispanic", "Asian", "Others"])
gender = st.selectbox("Gender:",  options = ["Male", "Female"])
metformin = st.selectbox("Was metformin prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
repaglinide = st.selectbox("Was repaglinide prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
nateglinide = st.selectbox("Was nateglinide prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
chlorpropamide = st.selectbox("Was chlorpropamide prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
glimepiride = st.selectbox("Was glimepiride prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
acetohexamide =  st.selectbox("Was acetohexamide prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
glipizide = st.selectbox("Was glipizide prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
glyburide = st.selectbox("Was glyburide prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
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
metformin_rosiglitazone = st.selectbox("Was metformin_rosiglitazone prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
metformin_pioglitazone = st.selectbox("Was metformin_pioglitazone prescribed or was there a change in the dosage?:", options = ["Up", "Down", "Steady", "No"])
change = st.selectbox("Was there a change in diabetic medications?:", options = ["No", "Yes"])
diabetesmed = st.selectbox("Was there any diabetic medication prescribed?:", options = ["No", "Yes"])


    
def label_encode_admission_type(admission_type):
    # Define the mapping of admission types to numbers
    admission_type_mapping = {
        "Emergency": 1,
        "Urgent": 2,
        "Elective": 3,
        "Newborn": 4,
        "Routine": 5,
        "Pre-scheduled": 6,
        "Transfer": 7,
        "Not Available": 8
    }
    
    # Return the encoded value or None if the type is not found
    return admission_type_mapping.get(admission_type, None)


admission_type_id = label_encode_admission_type(selected_admission_type)

