import pickle
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('penyakit_kanker.sav','rb'))

#judul web 
st.text ('Niken Fauziah / 191351066 / Malam A')
st.title('Breast Cancer Prediction')

mean_radius = st.number_input('Input mean radius')

mean_texture = st.number_input('Input mean texture')

mean_perimeter = st.number_input('Input mean perimeter')

mean_area = st.number_input('Input mean area')

mean_smoothness = st.number_input('Input mean smoothness')

# code for prediction
kanker_diagnosis =''

# membuat tombol prediksi
if st.button('Breast Cancer Prediction'):
    kanker_prediction = model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness]])

    if (kanker_prediction[0]==1):
        kanker_diagnosis = 'Pasien Terkena Penyakit Kanker Payudara'
    else:
        kanker_diagnosis = 'Pasien Tidak Terkena penyakit Kanker Payudara'
st.success(kanker_diagnosis)