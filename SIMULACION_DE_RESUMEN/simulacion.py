import matplotlib.animation as animation
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

# =====================================================================
# CONFIGURACIÓN DE ESTILO (Look académico idéntico al PDF)
# =====================================================================
# Modificamos los parámetros globales de Matplotlib para darle una estética de reporte formal
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 12,
    'font.family': 'serif' # Fuente clásica con serifas para look tipo LaTeX
})

# =====================================================================
# ANIMACIÓN 1: CAMINATA ALEATORIA EN 2D 
# =====================================================================
print("Corriendo Animación 1: Caminata Aleatoria en 2D...")
print("--> Cierra esta ventana gráfica para avanzar automáticamente a la Animación 2.")

np.random.seed(42) # Semilla fija para reproducir la trayectoria 
n_steps = 10000    # Total de pasos discretos en la red

# En cada paso elegimos avanzar aleatoriamente -1 o 1 de forma equiprobable
steps_x = np.random.choice([-1, 1], size=n_steps)
steps_y = np.random.choice([-1, 1], size=n_steps)

# np.cumsum realiza la suma acumulada de los pasos; así obtenemos las coordenadas (X, Y) en cada instante
path_x = np.concatenate([[0], np.cumsum(steps_x)])
path_y = np.concatenate([[0], np.cumsum(steps_y)])

# Inicialización de la figura 1 (Lienzo para la caminata)
fig1, ax1 = plt.subplots(figsize=(6, 5.5))
ax1.set_facecolor('#f4f4f4')
ax1.set_xlabel("Eje X")
ax1.set_ylabel("Eje Y")
ax1.grid(True, color='white', linestyle='--', linewidth=1, zorder=0)

# Fijamos los límites de los ejes desde el inicio para que la ventana no parpadee ni cambie de tamaño al animarse
ax1.set_xlim(np.min(path_x) - 5, np.max(path_x) + 5)
ax1.set_ylim(np.min(path_y) - 5, np.max(path_y) + 5)

# Definimos los objetos gráficos vacíos que se actualizarán cuadro por cuadro
line, = ax1.plot([], [], color='#1f77b4', linewidth=0.6, label='Trayectoria', zorder=2)
ax1.scatter(0, 0, color='red', marker='o', s=50, label='Inicio (0,0)', zorder=3)
current_dot = ax1.scatter([], [], color='black', marker='X', s=50, label='Posición Actual', zorder=4)
ax1.legend(loc='upper left')

def init1():
    """Función de inicio obligatoria para FuncAnimation (con blit=True).
    Se encarga de limpiar o vaciar los datos de la línea y el marcador antes del primer cuadro."""
    line.set_data([], [])
    current_dot.set_offsets(np.empty((0, 2)))
    return line, current_dot

def update1(frame):
    """Función que dibuja la caminata cuadro por cuadro.
    'frame' es el número de cuadro actual que va arrojando el generador."""
    # Como animar 10,000 pasos de uno en uno sería lentísimo, multiplicamos por 10
    # para renderizar bloques de 10 pasos en cada frame, haciéndola súper veloz.
    actual_step = min(frame * 10, n_steps)
    
    # Actualizamos los datos de la línea azul agregando el nuevo bloque de posiciones recorrido
    line.set_data(path_x[:actual_step], path_y[:actual_step])
    
    # Movemos el marcador negro 'X' a la coordenada exacta del último paso renderizado
    current_dot.set_offsets(np.array([[path_x[actual_step-1], path_y[actual_step-1]]]))
    
    # Actualizamos el título dinámico mostrando el avance exacto de la caminata
    ax1.set_title(f"Simulación de una Caminata Aleatoria en \\mathbb{{Z}}^2 — Paso: {actual_step}")
    return line, current_dot

# Ejecutamos la primera animación. 
# interval=1 es el retraso en milisegundos entre cuadros para que vaya a máxima velocidad.
ani1 = animation.FuncAnimation(
    fig1, update1, frames=range(1, (n_steps // 10) + 1), 
    init_func=init1, interval=1, blit=True, repeat=False
)
plt.tight_layout()
plt.show()  # El script lineal de Python se detiene aquí. No avanzará hasta que el usuario cierre manualmente esta ventana.
plt.close()


# =====================================================================
# ANIMACIÓN 2: CONVERGENCIA DE LA CAMPANA (TEOREMA DEL LÍMITE CENTRAL)
# =====================================================================
print("\nVentana 1 cerrada. Corriendo Animación 2: Verificación del TLC...")

n_variables = 10  # Número máximo de variables aleatorias independientes a sumar
n_samples = 30000 # Cantidad de experimentos para construir un histograma suave y bien definido

# Generamos una matriz de datos uniformes centrados en 0 y con Varianza = 1 (Rango: [-sqrt(3), sqrt(3)])
data = np.random.uniform(-np.sqrt(3), np.sqrt(3), size=(n_samples, n_variables))

# Inicialización de la figura 2 (Lienzo para el TLC)
fig2, ax2 = plt.subplots(figsize=(6, 4.5))
ax2.set_facecolor('#f4f4f4')
ax2.set_xlabel("Valor")
ax2.set_ylabel("Densidad de Probabilidad")
ax2.set_xlim(-4.5, 4.5)
ax2.set_ylim(0, 0.43)
ax2.grid(True, color='white', linestyle='--', linewidth=1, zorder=0)

# Dibujamos de fondo la curva teórica de la Normal estándar N(0,1), la cual permanecerá fija
x_teorica = np.linspace(-4.5, 4.5, 200)
p_teorica = 1 / np.sqrt(2 * np.pi) * np.exp(-x_teorica**2 / 2)
ax2.plot(x_teorica, p_teorica, 'k-', linewidth=1.5, label='Normal Teórica \\mathcal{{N}}(0,1)', zorder=3)

# Creamos una leyenda personalizada usando un parche verde para representar de antemano el histograma animado
green_patch = mpatches.Patch(color='#2ca02c', alpha=0.6, label='Suma Normalizada')
ax2.legend(handles=[green_patch, ax2.lines[0]], loc='upper left')

def update2(frame):
    """Función que actualiza el histograma del TLC sumando una variable extra en cada cuadro.
    'frame' representa directamente cuántas variables (de 1 a 10) se están promediando."""
    # PASO CRÍTICO: Eliminamos las barras (patches) del histograma anterior.
    # Si no lo hiciéramos, los nuevos histogramas se encimarían sobre los viejos borrando el efecto visual.
    for patch in ax2.patches:
        patch.remove()
        
    # Implementación matemática del TLC:
    if frame == 1:
        # En el primer cuadro, simplemente tomamos la primera columna (distribución uniforme original)
        sum_actual = data[:, 0]
    else:
        # En los siguientes cuadros, sumamos las columnas hasta el índice actual y normalizamos dividiendo entre sqrt(n)
        sum_actual = np.sum(data[:, :frame], axis=1) / np.sqrt(frame)
        
    # Volvemos a trazar el histograma con los 80 contenedores (bins) y la densidad de probabilidad activada
    ax2.hist(sum_actual, bins=80, density=True, alpha=0.6, color='#2ca02c', zorder=2)
    
    # CORRECCIÓN DE SEGURIDAD: Usamos .format() para inyectar la variable de forma segura.
    # Esto evita que Python confunda los símbolos de '$' de LaTeX con variables del f-string.
    ax2.set_title("Demostración del TLC (Convergencia de Lindeberg) — $n = {}$".format(frame))

# Ejecutamos la segunda animación. 
# interval=1200 (1.2 segundos por cuadro) para que el público aprecie cómo cambia la forma geométrica en cada paso.
ani2 = animation.FuncAnimation(
    fig2, update2, frames=range(1, n_variables + 1), 
    interval=1200, repeat=True, blit=False # blit=False es obligatorio aquí ya que el histograma regenera objetos dinámicamente
)
plt.tight_layout()
plt.show()
plt.close()