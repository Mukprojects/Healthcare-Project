import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Configure Page
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️", layout="centered")

# Hide Default Streamlit UI Elements
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Background Styling
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://img.freepik.com/free-photo/close-up-people-wearing-lab-coats_23-2149126948.jpg?t=st=1741666018~exp=1741669618~hmac=f14b42856064e9af2bbdbb9049534129ae4f76f30479dec26cc5938b4f3777f4&w=1380");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.6);
    }
    </style>
    """, unsafe_allow_html=True)

# Load Models
models = {
    'Diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'Heart Disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'Parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'Lung Cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'Hypo-Thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# Sidebar Navigation
selected = st.sidebar.selectbox("Select a Disease to Predict", list(models.keys()))

st.title(f"{selected} Prediction")
st.write("Enter the required details below to predict the outcome.")

def get_input(label, key, type="number"):
    return st.number_input(label, key=key, step=1) if type == "number" else st.text_input(label, key=key)

# Disease-Specific Input Fields
input_features = {}

disease_parameters = {
    "Diabetes": ["Pregnancies", "Glucose", "Blood Pressure", "Skin Thickness", "Insulin", "BMI", "Diabetes Pedigree Function", "Age"],
    "Heart Disease": ["Age", "Sex (1=Male, 0=Female)", "Chest Pain Type (0-3)", "Resting BP", "Cholesterol", "Fasting Blood Sugar (1=True, 0=False)", "Resting ECG (0-2)", "Max Heart Rate", "Exercise Induced Angina (1=Yes, 0=No)", "ST Depression", "Slope (0-2)", "Major Vessels (0-3)", "Thal (0-2)"],
    "Parkinsons": ["MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)", "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR", "RPDE", "DFA", "Spread1", "Spread2", "D2", "PPE"],
    "Lung Cancer": ["Gender (1=Male, 0=Female)", "Age", "Smoking (1=Yes, 0=No)", "Yellow Fingers", "Anxiety", "Peer Pressure", "Chronic Disease", "Fatigue", "Allergy", "Wheezing", "Alcohol Consuming", "Coughing", "Shortness of Breath", "Swallowing Difficulty", "Chest Pain"],
    "Hypo-Thyroid": ["Age", "Sex (1=Male, 0=Female)", "On Thyroxine (1=Yes, 0=No)", "TSH Level", "T3 Measured (1=Yes, 0=No)", "T3 Level", "TT4 Level"]
}

for param in disease_parameters[selected]:
    input_features[param] = get_input(param, param.replace(" ", "_"))

# Prediction
if st.button(f"Predict {selected}"):
    model = models[selected]
    prediction = model.predict([list(input_features.values())])[0]
    result = f"The person has {selected}" if prediction == 1 else f"The person does not have {selected}"
    st.success(result)

# Footer Styling
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            color: white;
            text-align: center;
            padding: 10px;
        }
    </style>
    <div class="footer">
        <p>Developed with ❤️ by AI Developer</p>
    </div>
    """, unsafe_allow_html=True)
