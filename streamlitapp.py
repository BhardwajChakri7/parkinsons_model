import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
parkinsons_model = pickle.load(open('parkinson_model.sav', 'rb'))

# Page title
st.title("Parkinson's Disease Prediction using ML")

# Add CSS for full background image
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://raw.githubusercontent.com/SHAIK-RAIYAN-2022-CSE/malaria/main/Images-free-abstract-minimalist-wallpaper-HD.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0);
}
.block-container {
    background: rgba(0, 0, 0, 0.5);
    padding: 20px;
    border-radius: 15px;
    max-width: 800px;
    margin: auto;
    backdrop-filter: blur(10px);
    box-shadow: 0px 6px 24px rgba(0, 0, 0, 0.8);
}
.stButton>button {
    background-color: #FF6347;
    color: white;
    font-size: 18px;
    padding: 10px 24px;
    border-radius: 10px;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: white;
    color: #FF6347;
    border: 2px solid #FF6347;
}
h1, h2, h3, h4, h5, h6, p {
    color: white;
    text-align: center;
}
</style>
''',
    unsafe_allow_html=True
)

# Layout for input fields
col1, col2, col3, col4, col5 = st.columns(5)  

with col1:
    fo = st.text_input('MDVP:Fo(Hz)')
    
with col2:
    fhi = st.text_input('MDVP:Fhi(Hz)')
    
with col3:
    flo = st.text_input('MDVP:Flo(Hz)')
    
with col4:
    Jitter_percent = st.text_input('MDVP:Jitter(%)')
    
with col5:
    Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    
with col1:
    RAP = st.text_input('MDVP:RAP')
    
with col2:
    PPQ = st.text_input('MDVP:PPQ')
    
with col3:
    DDP = st.text_input('Jitter:DDP')
    
with col4:
    Shimmer = st.text_input('MDVP:Shimmer')
    
with col5:
    Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    
with col1:
    APQ3 = st.text_input('Shimmer:APQ3')
    
with col2:
    APQ5 = st.text_input('Shimmer:APQ5')
    
with col3:
    APQ = st.text_input('MDVP:APQ')
    
with col4:
    DDA = st.text_input('Shimmer:DDA')
    
with col5:
    NHR = st.text_input('NHR')
    
with col1:
    HNR = st.text_input('HNR')
    
with col2:
    RPDE = st.text_input('RPDE')
    
with col3:
    DFA = st.text_input('DFA')
    
with col4:
    spread1 = st.text_input('spread1')
    
with col5:
    spread2 = st.text_input('spread2')
    
with col1:
    D2 = st.text_input('D2')
    
with col2:
    PPE = st.text_input('PPE')

# Code for Prediction
parkinsons_diagnosis = ''

# Creating a button for Prediction    
if st.button("Parkinson's Test Result"):
    parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])                          
    
    if parkinsons_prediction[0] == 1:
        parkinsons_diagnosis = "The person has Parkinson's disease"
    else:
        parkinsons_diagnosis = "The person does not have Parkinson's disease"
    
st.success(parkinsons_diagnosis)
