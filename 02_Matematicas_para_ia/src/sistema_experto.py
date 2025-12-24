import pandas as pd
import numpy as np
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

class SistemaExpertoSalud:
    
    def __init__(self):
        self.modelo = None
        
        # --- MAPEO EXACTO DE LA RUTA ---
        # 1. Obtenemos la ubicación de este archivo script (sistema_experto.py)
        directorio_src = os.path.dirname(os.path.abspath(__file__))
        
        # 2. Construimos la ruta hacia la carpeta 'data'
        # Subimos un nivel (..) y entramos a 'data'
        # Ajusta el nombre del archivo si tu Excel se llama diferente
        nombre_archivo = "dataset_registros.xlsx"
        self.ruta_archivo = os.path.join(directorio_src, "..", "data", nombre_archivo)
        
    def cargar_y_entrenar(self):
        print("🧠 1. Iniciando Sistema Experto...")
        print(f"    📂 Buscando archivo en: {self.ruta_archivo}")
        
        # VERIFICACIÓN DE EXISTENCIA
        if not os.path.exists(self.ruta_archivo):
            print("\n    ❌ ERROR DE RUTA: No encuentro el archivo.")
            print(f"    ⚠️ El sistema busca en: {self.ruta_archivo}")
            print("    💡 Solución: Verifica que el archivo esté en la carpeta 'data' y el nombre sea exacto.")
            return False

        # CARGA DE EXCEL
        try:
            # engine='openpyxl' es necesario para leer archivos .xlsx
            df = pd.read_excel(self.ruta_archivo, engine='openpyxl')
            print(f"    ✅ Archivo Excel cargado: {len(df)} registros encontrados.")
        except ImportError:
            print("\n    ❌ ERROR DE LIBRERÍA: Falta 'openpyxl'.")
            print("    💡 Solución: Escribe en tu terminal: pip install openpyxl")
            return False
        except Exception as e:
            print(f"    ❌ Error inesperado al leer Excel: {e}")
            return False

        print("🧠 2. Entrenando IA (Árbol de Decisión)...")
        
        # --- LIMPIEZA Y ENTRENAMIENTO (Igual que antes) ---
        # Ingeniería de Variables (Rellenar huecos)
        cols_numericas = ['Altura_cm', 'Peso_kg', 'Nivel_Glucosa', 'Horas_Sueno']
        for col in cols_numericas:
            if col in df.columns:
                df[col] = df[col].fillna(df[col].mean())
        
        # Calcular IMC
        df['IMC'] = df['Peso_kg'] / ((df['Altura_cm'] / 100) ** 2)

        # Limpiar Objetivo
        if 'Riesgo_Salud' not in df.columns:
             print("    ❌ Error: Tu Excel no tiene la columna 'Riesgo_Salud'.")
             return False
             
        df_clean = df.dropna(subset=['Riesgo_Salud'])

        # Definir X (Factores) e y (Objetivo)
        X = df_clean[['IMC', 'Nivel_Glucosa', 'Horas_Sueno']]
        y = df_clean['Riesgo_Salud']

        # Entrenar
        self.modelo = DecisionTreeClassifier(max_depth=5)
        self.modelo.fit(X, y)
        
        print("    ✅ Modelo entrenado y listo para diagnósticos.")
        return True

    def analizar_paciente(self, altura_cm, peso_kg, glucosa, horas_sueno):
        # A. Análisis Matemático (Peso Ideal - Fórmula de Lorentz/BMI)
        peso_ideal = 22 * ((altura_cm / 100) ** 2)
        diferencia = peso_kg - peso_ideal
        
        # B. Diagnóstico de IA
        imc_actual = peso_kg / ((altura_cm / 100) ** 2)
        datos_paciente = pd.DataFrame([[imc_actual, glucosa, horas_sueno]], 
                                      columns=['IMC', 'Nivel_Glucosa', 'Horas_Sueno'])
        
        prediccion_riesgo = self.modelo.predict(datos_paciente)[0]
        
        # C. Generar Reporte
        print("\n" + "="*45)
        print(f"📋 REPORTE DIAGNÓSTICO (Paciente: {altura_cm}cm, {peso_kg}kg)")
        print("="*45)
        print(f"🔹 Peso Ideal Aprox: {peso_ideal:.1f} kg")
        
        if diferencia > 5: print(f"⚠️  Estado: Sobrepeso (+{diferencia:.1f} kg)")
        elif diferencia < -5: print(f"⚠️  Estado: Bajo peso (-{abs(diferencia):.1f} kg)")
        else: print("✅  Estado: Peso saludable")

        print(f"\n🔹 Predicción de Riesgo (IA): {prediccion_riesgo.upper()}")
        
        print("🔍 Factores Analizados:")
        if glucosa > 100: print(f"   • Glucosa Alta ({glucosa} mg/dl)")
        if horas_sueno < 6: print(f"   • Sueño Insuficiente ({horas_sueno} hrs)")
        if imc_actual > 25: print(f"   • IMC Elevado ({imc_actual:.1f})")
        if glucosa <= 100 and horas_sueno >= 6 and imc_actual <= 25:
            print("   • Todos los indicadores vitales en orden.")
        
        print("="*45 + "\n")

# --- EJECUCIÓN ---
if __name__ == "__main__":
    app = SistemaExpertoSalud()
    if app.cargar_y_entrenar():
        print("\n--- 🏥 MODO INTERACTIVO (Escribe los datos) ---")
        try:
            a = float(input("1. Altura (cm): "))
            p = float(input("2. Peso (kg): "))
            g = float(input("3. Glucosa (mg/dl): "))
            s = float(input("4. Horas de Sueño: "))
            
            app.analizar_paciente(a, p, g, s)
        except ValueError:
            print("❌ Error: Debes ingresar solo números.")
    else:
        print("\n❌ EL PROGRAMA FALLÓ.")
        print("\n❌ EL PROGRAMA FALLÓ.")