import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Cargar dataset
df = pd.read_csv("data/frecuencias_combinadas.csv")

# Codificar variables categóricas
le_dia = LabelEncoder()
le_ciudad = LabelEncoder()
df["dia"] = le_dia.fit_transform(df["dia"])
df["ciudad"] = le_ciudad.fit_transform(df["ciudad"])

# Características y etiqueta
X = df[["hora", "dia", "ciudad"]]
y = df["frecuencia_mhz"].astype(int)

# Dividir dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Predecir
y_pred = clf.predict(X_test)

# Reporte de clasificación
print("Reporte de clasificación:\n")
print(classification_report(y_test, y_pred))

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred)

# Visualización de la matriz de confusión
plt.figure(figsize=(10,7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Matriz de Confusión")
plt.xlabel("Predicción")
plt.ylabel("Etiqueta Verdadera")
plt.show()

# Guardar modelo y codificadores
joblib.dump(clf, "model/model_report.pkl")
joblib.dump(le_dia, "model/encoder_dia_report.pkl")
joblib.dump(le_ciudad, "model/encoder_ciudad_report.pkl")
