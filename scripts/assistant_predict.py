import joblib
import pandas as pd

# Cargar el modelo entrenado con Pipeline (ya incluye OneHotEncoder)
model = joblib.load("model/model_combined.pkl")

def predict_frequencies(hora: int, dia: str, ciudad: str, actividad=1):
    # Crear DataFrame con las mismas columnas que usó el modelo
    data = {
        "hora": [hora],
        "dia": [dia],
        "ciudad": [ciudad],
        "actividad": [actividad]
    }
    X = pd.DataFrame(data)  # ✅ Requiere nombres de columna exactos
    freq_pred = model.predict(X)
    return freq_pred[0]

if __name__ == "__main__":
    hora = 21
    dia = "Tuesday"  # ⚠️ Usa el mismo idioma y formato que en los datos de entrenamiento
    ciudad = "Madrid"
    actividad = 1  

    frecuencia = predict_frequencies(hora, dia, ciudad, actividad)
    print(f"📡 Frecuencia recomendada para escanear a las {hora}:00 del {dia} en {ciudad}: {frecuencia:.2f} MHz")
