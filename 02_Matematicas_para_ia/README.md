# 📊 Módulo 02: Matemáticas para IA (Análisis de Datos)

> **"Los datos son el nuevo petróleo, pero las matemáticas son la refinería."**

## 🎯 Objetivo del Proyecto

Dejar atrás la intuición y usar **Estadística y Probabilidad** para tomar decisiones. En este módulo, actuamos como Científicos de Datos para analizar un dataset de 1,000 pacientes, limpiar la información incompleta y generar diagnósticos automáticos.

---

## 📂 Niveles de Evolución del Código

Este proyecto demuestra que no siempre "más complejo" es mejor. A veces, una regresión lineal falla donde un árbol de decisión triunfa.

| Nivel                  | Archivo                        | Concepto Clave                                                                                                  | Estado          |
| :--------------------- | :----------------------------- | :-------------------------------------------------------------------------------------------------------------- | :-------------- |
| **1. Fundamentos**     | `1_analisis_fundamentos.ipynb` | **NumPy**: Calcular promedios y desviaciones "a mano" para entender la fórmula.                                 | ✅ Didáctico    |
| **2. Exploración**     | `1_analisis_fundamentos.ipynb` | **Pandas**: Visualizar correlaciones y filtrar datos masivos.                                                   | ✅ Visual       |
| **3. Predicción**      | `src/analisis_salud.py`        | **Regresión Lineal**: Intentar predecir peso basado en altura (y descubrir por qué falla con datos aleatorios). | ⚠️ Experimental |
| **4. Sistema Experto** | `src/sistema_experto.py`       | **POO + Árboles**: Un sistema inteligente (`Class`) que cruza 4 variables para diagnosticar riesgos.            | 🚀 Producción   |

---

## 💡 Lecciones Aprendidas (Troubleshooting)

### ¿Por qué falló la predicción de Peso en el Nivel 3?

Descubrimos que en nuestro dataset sintético, la correlación entre Altura y Peso era cercana a **0**.

- **Lección de Oro:** "Garbage In, Garbage Out". Si los datos no tienen patrón, la IA no puede inventarlo.
- **Solución (Nivel 4):** Pivotamos a un **Modelo Normativo** (Fórmulas médicas de IMC) y un **Clasificador de Riesgo**, demostrando que un Ingeniero de IA debe adaptarse a sus datos.

---

## 🚀 Instrucciones de Ejecución

### Para ver las gráficas (Nivel 2)

1. Abrir `notebooks/1_analisis_fundamentos.ipynb` en VS Code.
2. Ejecutar todas las celdas.

### Para correr el Sistema Experto (Nivel 4)

Este script te pedirá datos de un paciente y generará un reporte médico en tiempo real.

```bash
# Desde la terminal en la carpeta raíz:
python 02_Matematicas_IA/src/sistema_experto.py
```
