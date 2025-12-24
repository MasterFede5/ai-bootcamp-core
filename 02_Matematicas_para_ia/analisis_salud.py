
# análisis_salud.py
import pandas as pd
import numpy as np

# --- CONFIGURACIÓN ---
RUTA_ARCHIVO = "data/dataset_registros.xlsx"

def cargar_datos(ruta):
    """Carga el excel y maneja errores si no existe."""
    try:
        df = pd.read_excel(ruta)
        print(f"✅ Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas.")
        return df
    except FileNotFoundError:
        print("❌ Error: Archivo no encontrado. Revisa la carpeta 'data'.")
        return None

def limpieza_matematica(df):
    """
    Rellena valores nulos usando estadística (Promedio y Moda).
    No eliminamos filas, 'reparamos' los datos.
    """
    print("\n --- INICIANDO LIMPIEZA DE DATOS ---")
    
    # 1. Diagnóstico Inicial
    nulos = df.isnull().sum()
    print(f"Datos vacíos detectados:\n{nulos[nulos > 0]}")

    # 2. Imputación de Numéricos (Usamos la MEDIA/PROMEDIO)
    # Si no sabemos la altura, asumimos el promedio. Es lo estadísticamente neutro.
    cols_numericas = ["Altura_cm", "Peso_kg", "Horas_Sueno", "Nivel_Glucosa"]
    
    for col in cols_numericas:
        if col in df.columns:
            promedio = df[col].mean()
            df[col] = df[col].fillna(promedio)
            print(f"Columna '{col}': Rellenados huecos con promedio ({promedio:.1f})")

    # 3. Imputación de Categorías (Usamos la MODA/LO MÁS COMÚN)
    # Si no sabemos el riesgo, ponemos el más común del grupo.
    cols_texto = ["Riesgo_Salud", "Actividad_Fisica"]
    
    for col in cols_texto:
        if col in df.columns:
            moda = df[col].mode()[0] # El valor más repetido
            df[col] = df[col].fillna(moda)
            print(f"Columna '{col}': Rellenados huecos con moda ('{moda}')")

    return df

def prediccion_simple(df):
    """
    Usa Álgebra Lineal básica (y = mx + b) para encontrar patrones.
    Predicción: ¿Cuánto deberías pesar según tu altura?
    """
    print("\ --- MODELO MATEMÁTICO DE PREDICCIÓN ---")
    
    # Extraemos datos limpios
    x = df["Altura_cm"].values
    y = df["Peso_kg"].values

    # Ajuste Polinómico de Grado 1 (Línea Recta: Regresión Lineal)
    # NumPy calcula la pendiente (m) y la intersección (b)
    m, b = np.polyfit(x, y, 1)

    print(f"Fórmula descubierta: Peso = ({m:.2f} * Altura) + {b:.2f}")
    print("Esto significa que por cada cm extra de altura, el peso aumenta aprox " + f"{m:.2f} kg.")

    return m, b

def main():
    # 1. Cargar
    df = cargar_datos(RUTA_ARCHIVO)
    if df is None: return

    # 2. Limpiar (Nivel 3)
    df_limpio = limpieza_matematica(df)

    # 3. Predecir
    m, b = prediccion_simple(df_limpio)

    # 4. Prueba Interactiva
    print("\n--- PRUEBA TU PROPIA PREDICCIÓN ---")
    try:
        mi_altura = float(input("Introduce tu altura en cm (ej: 175): "))
        peso_estimado = (m * mi_altura) + b
        print(f"Según mis cálculos matemáticos, deberías pesar aprox: {peso_estimado:.1f} kg")
    except ValueError:
        print("Error: Introduce un número válido.")

if __name__ == "__main__":
    main()