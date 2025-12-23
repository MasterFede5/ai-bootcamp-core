# Módulo 01: Pensamiento Algorítmico y Programación para IA

> **"Antes de enseñar a una computadora a pensar, debemos enseñarle a obedecer."**

## 📘 El Código Detrás de la Inteligencia

En este primer módulo, aprendemos el arte de dar instrucciones claras a una máquina. Usamos **Python**, el lenguaje estándar de la IA, para resolver problemas lógicos mediante algoritmos.

### 🐭 El Proyecto: Laberinto Virtual

El objetivo no es solo crear un juego, sino entender los fundamentos de los **Agentes Inteligentes**:

1.  **Entorno:** El laberinto (Matriz de datos).
2.  **Estado:** ¿Dónde estoy? (Coordenadas X, Y).
3.  **Acción:** ¿A dónde voy? (Inputs y Condicionales).

---

## 📂 Estructura del Proyecto

Este módulo se ha desarrollado en 3 niveles de complejidad técnica:

| Nivel              | Archivo                                              | Descripción                                                    |
| :----------------- | :--------------------------------------------------- | :------------------------------------------------------------- |
| **1. Lógica Pura** | _Incluido en el Notebook_                            | Entender coordenadas (x, y) sin gráficos.                      |
| **2. Explorador**  | `notebooks/1_laberinto_didactico.ipynb`              | Uso de **Jupyter Notebook** y emojis para visualizar matrices. |
| **3. Ingeniería**  | `src/2_laberinto:class.py` y ´src/laberinto_game.py´ | Implementación profesional con **Clases (POO)** y modularidad. |

## 🚀 Instrucciones de Ejecución

### Para la Versión Didáctica (Notebook)

1. Abre VS Code.
2. Instala la extensión "Jupyter".
3. Abre el archivo `notebooks/1_laberinto_didactico.ipynb`.
4. Haz clic en el botón ▶️ (Play) en la primera celda.

### Para la Versión Profesional (Terminal)

Si quieres sentirte como un verdadero ingeniero de software, ejecuta el juego desde la consola:

```bash
# Asegúrate de estar en la carpeta raíz 'ai-bootcamp-core'
python 01_Pensamiento_Algoritmico/src/maze_oop.py
```

###TECNOLOGÍAS UTILIZADAS

- Python
- Jupyter Notebook
- POO (Programación Orientada a Objetos)
