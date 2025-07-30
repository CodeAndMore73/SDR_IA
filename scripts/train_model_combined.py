import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Cargar datos
df = pd.read_csv("data/frecuencias_combinadas.csv")

# Separar características (X) y etiqueta (y)
X = df[["hora", "dia", "ciudad"]]
y = df["frecuencia_mhz"]  # <- esto es continuo, así que es un problema de regresión

# Definir columnas categóricas (para codificación one-hot)
categorical_features = ["dia", "ciudad"]

# Crear el preprocesador para convertir texto a números
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ],
    remainder="passthrough"  # deja 'hora' y 'actividad' como están
)

# Crear el pipeline con preprocesamiento y regresor
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=100, random_state=42))
])

# Dividir en train/test (opcional pero recomendado)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model.fit(X_train, y_train)

# Guardar el modelo
joblib.dump(model, "model/model_combined.pkl")

print("✅ Modelo entrenado y guardado correctamente como 'model/model_combined.pkl'")
