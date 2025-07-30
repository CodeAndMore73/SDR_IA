import subprocess
import pandas as pd
from datetime import datetime
import os

OUTPUT_FILE = "data/rtl_power_log.csv"

# Configura tus parámetros de escaneo
FREQ_RANGE = "100M:1500M:1M"  # De 100 MHz a 1500 MHz, con resolución de 1 MHz
THRESHOLD_DB = -50  # Nivel mínimo de señal para considerar que hay actividad

def get_current_time_info():
    now = datetime.now()
    return now.hour, now.strftime("%A")

def run_rtl_power():
    print("⏳ Escaneando espectro con rtl_power...")
    try:
        result = subprocess.run(
            ["rtl_power", "-f", FREQ_RANGE, "-g", "20", "-i", "5", "-c", "1"],
            capture_output=True, text=True, timeout=20
        )
        return result.stdout.strip().split("\n")
    except Exception as e:
        print("Error ejecutando rtl_power:", e)
        return []

def parse_output(lines):
    rows = []
    hour, day = get_current_time_info()
    city = "Madrid"

    for line in lines:
        if line.startswith("#") or not line.strip():
            continue
        parts = line.split(",")
        if len(parts) < 7:
            continue
        start_freq = float(parts[2])
        bin_width = float(parts[3])
        power_values = list(map(float, parts[6:]))

        for i, db in enumerate(power_values):
            freq = start_freq + i * bin_width
            actividad = 1 if db > THRESHOLD_DB else 0
            if actividad:
                rows.append({
                    "hora": hour,
                    "dia": day,
                    "ciudad": city,
                    "frecuencia_mhz": round(freq / 1e6, 2),
                    "actividad": actividad
                })

    return pd.DataFrame(rows)

def append_to_csv(df):
    if df.empty:
        print("📭 No se detectó actividad significativa.")
        return
    file_exists = os.path.exists(OUTPUT_FILE)
    df.to_csv(OUTPUT_FILE, mode="a", header=not file_exists, index=False)
    print(f"✅ {len(df)} registros guardados en el dataset.")

if __name__ == "__main__":
    output = run_rtl_power()
    df = parse_output(output)
    append_to_csv(df)
