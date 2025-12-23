import os

# --- CONFIGURACIÓN ---
# Constantes para fácil modificación
PARED = "⬛"
CAMINO = "⬜"
JUGADOR = "🐭"
META = "🧀"

def limpiar_pantalla():
    """
    Limpia la consola para que el juego se vea fluido.
    Detecta si es Windows ('nt') o Mac/Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def crear_mapa():
    """
    Devuelve la estructura inicial del laberinto.
    """
    return [
        [JUGADOR, CAMINO, PARED, CAMINO, CAMINO],
        [PARED, CAMINO, PARED, CAMINO, PARED],
        [CAMINO, CAMINO, CAMINO, CAMINO, PARED],
        [CAMINO, PARED, PARED, CAMINO, CAMINO],
        [CAMINO, CAMINO, CAMINO, PARED, META]
    ]

def dibujar_mapa(mapa):
    """
    Recibe el mapa y lo imprime en pantalla línea por línea.
    """
    print("\nLaberinto: ¡Ayuda al ratón!")
    print("---------------------------")
    for fila in mapa:
        print("".join(fila))
    print("---------------------------")

def main():
    """
    Función principal que controla el ciclo del juego.
    """
    mapa = crear_mapa()
    fila_jugador, col_jugador = 0, 0
    jugando = True

    while jugando:
        # 1. Limpiar y dibujar
        limpiar_pantalla()
        dibujar_mapa(mapa)

        # 2. Verificar Victoria
        if mapa[fila_jugador][col_jugador] == META:
            print("\n🏆 ¡FELICIDADES! ¡El ratón encontró el queso! 🧀")
            break

        # 3. Input del usuario
        movimiento = input("Mueve (w/a/s/d) o 'q' para salir: ").lower()

        # 4. Calcular futuro movimiento
        f_nueva, c_nueva = fila_jugador, col_jugador

        if movimiento == 'w': f_nueva -= 1
        elif movimiento == 's': f_nueva += 1
        elif movimiento == 'a': c_nueva -= 1
        elif movimiento == 'd': c_nueva += 1
        elif movimiento == 'q': 
            print("Saliste del juego.")
            break
        
        # 5. Validaciones (Límites y Paredes)
        # Verificamos si se sale del rango de la lista (0 a 4)
        if f_nueva < 0 or f_nueva > 4 or c_nueva < 0 or c_nueva > 4:
            continue # Salta al inicio del ciclo (no mueve)
        
        if mapa[f_nueva][c_nueva] == PARED:
            continue # Choca con pared (no mueve)

        # 6. Mover al Jugador
        # Borrar rastro anterior (si no estamos sobre la meta)
        if mapa[fila_jugador][col_jugador] != META:
            mapa[fila_jugador][col_jugador] = CAMINO
        
        # Actualizar coordenadas
        fila_jugador, col_jugador = f_nueva, c_nueva
        
        # Dibujar en nueva posición
        if mapa[fila_jugador][col_jugador] != META:
            mapa[fila_jugador][col_jugador] = JUGADOR

# --- PUNTO DE ENTRADA ---
# Esta condición asegura que el juego solo arranque si ejecutamos este archivo directamente
if __name__ == "__main__":
    main()