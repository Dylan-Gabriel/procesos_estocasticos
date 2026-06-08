import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# CONFIGURACIÓN DE ESTILO EDITORIAL (Idéntico al PDF del Proyecto)
# =====================================================================
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 12,
    'font.family': 'serif'  # Fuente con serifas estilo LaTeX
})

# =====================================================================
# SIMULACIÓN 1: CONVERGENCIA DE LA SERIE DE FOURIER DE WIENER (PÁG. 6)
# =====================================================================
print("Generando Figura 1: Convergencia de la Serie de Fourier de Wiener...")

np.random.seed(42)  # Semilla exacta para calcar la curva del PDF
t1 = np.linspace(0, 1, 1000)
N_terms_list = [5, 20, 500]

# Pre-generamos las variables normales independientes Z_k ~ N(0,1)
Z = np.random.normal(0, 1, size=max(N_terms_list))

fig1, ax1 = plt.subplots(figsize=(6, 4.5))
ax1.set_facecolor('#f4f4f4')  # Fondo gris claro académico
ax1.grid(True, color='white', linestyle='--', linewidth=1, zorder=0)

for N in N_terms_list:
    W_t = np.zeros_like(t1)
    # Implementación rigurosa de la expansión de Karhunen-Loève del PDF
    for k in range(N):
        coef = (k + 0.5) * np.pi
        phi_k = np.sqrt(2) * np.sin(coef * t1) / coef
        W_t += Z[k] * phi_k
        
    # Asignación de etiquetas y colores coincidentes con tu reporte
    if N == 500:
        label = 'Suma Concluido (500 Términos)'
        color = '#2ca02c'  # Verde/Teal
        lw = 0.7
    elif N == 20:
        label = '20 Términos'
        color = '#ff7f0e'  # Naranja
        lw = 1.0
    else:
        label = '5 Términos'
        color = '#1f77b4'  # Azul
        lw = 1.2
        
    ax1.plot(t1, W_t, label=label, linewidth=lw, color=color, zorder=2)

ax1.set_title('Construcción de Wiener en $[0, 1]$ vía Fourier')
ax1.set_xlabel('Tiempo $t$')
ax1.set_ylabel('$W_t$')
ax1.legend(loc='upper left')
plt.tight_layout()
plt.savefig('wiener_fourier_construction.png', dpi=300)
plt.show()
plt.close()


# =====================================================================
# SIMULACIÓN 2: LEY DEL LOGARITMO ITERADO DE KHINCHIN (PÁG. 7)
# =====================================================================
print("Generando Figura 2: Ley del Logaritmo Iterado (LIL)...")

np.random.seed(101)  # Semilla de horizonte extendido
t2 = np.linspace(0, 2000, 10000)
dt = t2[1] - t2[0]

# Construcción de la trayectoria continua mediante incrementos del TCL
dW = np.random.normal(0, np.sqrt(dt), size=len(t2)-1)
W = np.concatenate([[0], np.cumsum(dW)])

fig2, ax2 = plt.subplots(figsize=(6.5, 4.2))
ax2.set_facecolor('#f4f4f4')
ax2.grid(True, color='white', linestyle='--', linewidth=1, zorder=0)

# Graficamos la trayectoria del proceso browniano en azul fino
ax2.plot(t2, W, color='#1f77b4', linewidth=0.5, label='Trayectoria $W_t$', zorder=2)

# Evaluamos la envoltura asintótica a partir de t=3 para evitar log(log(t)) <= 0
t_envelope = np.linspace(3, 2000, 5000)
envelope_upper = np.sqrt(2 * t_envelope * np.log(np.log(t_envelope)))
envelope_lower = -envelope_upper

# Graficamos las cotas asintóticas estrictas en rojo discontinuo
ax2.plot(t_envelope, envelope_upper, color='red', linestyle='--', linewidth=1.3, label=r'Límite LIL $\pm\sqrt{2t\log\log t}$', zorder=3)
ax2.plot(t_envelope, envelope_lower, color='red', linestyle='--', linewidth=1.3, zorder=3)

ax2.set_title('Ley del Logaritmo Iterado (LIL) para Envoltura Asintótica')
ax2.set_xlabel('Tiempo $t$')
ax2.set_ylabel('$W_t$')
ax2.legend(loc='upper left')
plt.tight_layout()
plt.savefig('lil_envelope_plot.png', dpi=300)
plt.show()
plt.close()

print("¡Ambas figuras guardadas en alta resolución (.png) con el diseño exacto!")