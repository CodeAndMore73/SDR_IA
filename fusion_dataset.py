import pandas as pd
import os

# Archivos de entrada
file_433 = "data/rtl433_log.csv"
file_power = "data/rtl_power_log.csv"
output_file = "data/frecuencias_combinadas.csv"

# Leer datasets si existen
df_list = []
if os.path.exists(file_433):
    df_433 = pd.read_csv(file_433)
    df_list.append(df_433)
else:
    print("⚠️ No se encontró rtl433_log.csv")

if os.path.exists(file_power):
    df_power = pd.read_csv(file_power)
    df_list.append(df_power)
else:
    print("⚠️ No se encontró rtl_power_log.csv")

# Unir datasets si hay alguno disponible
if df_list:
    df_combined = pd.concat(df_list, ignore_index=True)

    # Eliminar duplicados exactos (por seguridad)
    df_combined = df_combined.drop_duplicates()

    # Ordenar por hora y frecuencia
    df_combined = df_combined.sort_values(by=["hora", "frecuencia_mhz"])

    # Guardar archivo combinado
    df_combined.to_csv(output_file, index=False)
    print(f"✅ Dataset combinado guardado en: {output_file}")
    print(df_combined.head())
else:
    print("❌ No se encontraron datasets para combinar.")
