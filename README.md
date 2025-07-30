# 🛠️ Parte práctica – Asistente inteligente de frecuencias SDR + IA

Esta guía te ayudará a ejecutar paso a paso el asistente inteligente para RTL-SDR que predice qué frecuencia escanear según hora, día y ciudad.

---

## 📁 Estructura

```
frequency_ai_assistant_full/
├── data/
│   └── frecuencias_combinadas.csv
├── model/
│   ├── model_combined.pkl
│   ├── encoder_dia_combined.pkl
│   └── encoder_ciudad_combined.pkl
├── scripts/
│   └── assistant_predict.py
├── streamlit_assistant.py
└── README_practica.md
```

---

## 1️⃣ Revisar el dataset

```python
import pandas as pd
df = pd.read_csv("data/frecuencias_combinadas.csv")
print(df.head())
```

Estructura esperada:

```
frecuencia_mhz,hora,dia,ciudad
433.92,9,Lunes,Madrid
868.3,15,Martes,Barcelona
...
```

---

## 2️⃣ Entrenar el modelo (opcional, ya está entrenado)

```bash
python3 scripts/train_model_combined.py
```

Este paso crea:
- `model_combined.pkl`
- `encoder_dia_combined.pkl`
- `encoder_ciudad_combined.pkl`

---

## 3️⃣ Ejecutar predicción desde terminal

```bash
python3 scripts/assistant_predict.py
```

Salida esperada:

```
Frecuencia recomendada para escanear a las 21:00 del Martes en Madrid: 433.92 MHz
```

---

## 4️⃣ Usar la interfaz gráfica con Streamlit

```bash
streamlit run streamlit_assistant.py
```

Selecciona los parámetros y obtendrás una frecuencia recomendada automáticamente.

---

## 5️⃣ Verificación en vivo (manual)

1. Abre GQRX, SDR++ o tu software SDR favorito.
2. Introduce la frecuencia recomendada.
3. Observa si hay actividad en el espectro.
4. Cambia los valores y experimenta.

---

## 📈 Mejora continua

- Añade más filas al CSV con tus observaciones
- Vuelve a entrenar para mejorar la IA
- Integra mapas, dashboards o alertas

---

Este proyecto es totalmente extensible y educativo. ¡Explóralo!