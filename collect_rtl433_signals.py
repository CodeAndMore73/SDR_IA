import subprocess
import json
import pandas as pd
from datetime import datetime
import os

OUTPUT_FILE = "data/rtl433_log.csv"

def get_current_time_info():
    now = datetime.now()
    return now.hour, now.strftime("%A")

def run_rtl_433():
    try:
        result = subprocess.run(["rtl_433", "-F", "json", "-T", "10"], capture_output=True, text=True, timeout=15)
        lines = result.stdout.strip().split("\n")
        return [json.loads(line) for line in lines if line.strip()]
    except Exception as e:
        print("Error ejecutando rtl_433:", e)
        return []

def append_to_csv(data):
    hour, day = get_current_time_info()
    city = "Barcelona"  # Puedes cambiarlo o hacerlo dinámico

    rows = []
    for item in data:
        freq = item.get("frequency", 433.92)
        rows.append({
            "hora": hour,
            "dia": day,
            "ciudad": city,
            "frecuencia_mhz": round(freq / 1e6, 2),
            "actividad": 1
        })

    if not rows:
        return

    df = pd.DataFrame(rows)
    file_exists = os.path.exists(OUTPUT_FILE)
    df.to_csv(OUTPUT_FILE, mode='a', header=not file_exists, index=False)
    print(f"{len(rows)} registros añadidos al log.")

if __name__ == "__main__":
    print("Ejecutando rtl_433 y registrando señales...")
    detections = run_rtl_433()
    append_to_csv(detections)
