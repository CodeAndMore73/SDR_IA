import streamlit as st
from datetime import datetime
import joblib
import sklearn
print(sklearn.__version__)

model = joblib.load("model/model_combined.pkl")
le_dia = joblib.load("model/encoder_dia_combined.pkl")
le_ciudad = joblib.load("model/encoder_ciudad_combined.pkl")

def predict_frequencies(hora, dia, ciudad):
    dia_enc = le_dia.transform([dia])[0]
    ciudad_enc = le_ciudad.transform([ciudad])[0]
    X = [[hora, dia_enc, ciudad_enc]]
    freq_pred = model.predict(X)
    return freq_pred[0]

st.title("Asistente inteligente para frecuencias RTL-SDR")

hora = st.slider("Selecciona la hora", 0, 23, datetime.now().hour)
dia = st.selectbox("Selecciona el día", le_dia.classes_)
ciudad = st.selectbox("Selecciona la ciudad", le_ciudad.classes_)

if st.button("Predecir frecuencia"):
    frecuencia = predict_frequencies(hora, dia, ciudad)
    st.success(f"Frecuencia recomendada para escanear: {frecuencia} MHz")