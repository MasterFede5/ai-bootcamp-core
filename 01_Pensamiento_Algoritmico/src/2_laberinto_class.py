import os

# --- CONFIGURACIÓN GLOBAL ---
PARED = "⬛"
CAMINO = "⬜"
JUGADOR = "🐭"
META = "🧀"

class LaberintoEnv:
    """
    Esta clase representa el 'Entorno' del juego.
    Maneja el mapa, el estado del jugador y las reglas.
    """
    
    def __init__(self):
        """
        El CONSTRUCTOR: Se ejecuta automáticamente al crear el juego.
        Aquí definimos el estado inicial.
        """
        self.mapa = [
            [JUGADOR, CAMINO, PARED, CAMINO, CAMINO],
            [PARED, CAMINO, PARED, CAMINO, PARED],
            [CAMINO, CAMINO, CAMINO, CAMINO, PARED],
            [CAMINO, PARED, PARED, CAMINO, CAMINO],
            [CAMINO, CAMINO, CAMINO, PARED, META]
        ]
        self.fila_jugador = 0
        self.col_jugador = 0
        self.juego_activo = True

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def render(self):
        """
        Dibuja el estado actual del entorno en pantalla.
        """
        self.limpiar_pantalla()
        print("\n--- 🐭 Laberinto POO 🧀 ---")
        for fila in self.mapa:
            print("".join(fila))
        print("---------------------------")

    def step(self, accion):
        """
        El motor del juego. Recibe una acción (input) y actualiza el estado.
        Devuelve True si el juego terminó.
        """
        # 1. Calcular coordenadas tentativas
        f_nueva, c_nueva = self.fila_jugador, self.col_jugador
        
        if accion == 'w': f_nueva -= 1
        elif accion == 's': f_nueva += 1
        elif accion == 'a': c_nueva -= 1
        elif accion == 'd': c_nueva += 1
        elif accion == 'q': 
            print("Te has rendido.")
            self.juego_activo = False
            return

        # 2. Validar Movimiento (Lógica encapsulada)
        if self._es_movimiento_valido(f_nueva, c_nueva):
            self._mover_jugador(f_nueva, c_nueva)
            self._verificar_victoria()

    def _es_movimiento_valido(self, f, c):
        """Método privado (interno) para validar reglas."""
        # Regla de bordes
        if f < 0 or f > 4 or c < 0 or c > 4:
            return False
        # Regla de paredes
        if self.mapa[f][c] == PARED:
            return False
        return True

    def _mover_jugador(self, f, c):
        """Actualiza la matriz visual."""
        # Limpiar casilla anterior (si no es meta)
        if self.mapa[self.fila_jugador][self.col_jugador] != META:
            self.mapa[self.fila_jugador][self.col_jugador] = CAMINO
        
        # Actualizar coordenadas internas
        self.fila_jugador, self.col_jugador = f, c
        
        # Dibujar en nueva casilla (si no es meta)
        if self.mapa[f][c] != META:
            self.mapa[f][c] = JUGADOR

    def _verificar_victoria(self):
        if self.mapa[self.fila_jugador][self.col_jugador] == META:
            self.render() # Mostrar el último estado
            print("\n🏆 ¡MISIÓN CUMPLIDA! El agente ha llegado a la meta.")
            self.juego_activo = False

# --- EJECUCIÓN DEL JUEGO ---
if __name__ == "__main__":
    # 1. Instanciamos el objeto (Creamos el mundo)
    env = LaberintoEnv()
    
    # 2. Ciclo principal (Game Loop)
    while env.juego_activo:
        env.render()
        comando = input("Mueve (w/a/s/d) o 'q': ").lower()
        env.step(comando) # Le enviamos la acción al entorno