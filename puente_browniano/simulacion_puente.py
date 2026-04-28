import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Simulador Puente Browniano", layout="wide")
st.title("Simulador Interactivo: Puente Browniano")

st.sidebar.header("Parámetros de la Simulación")
M = st.sidebar.slider("Número de Trayectorias", min_value=5, max_value=1000, value=50, step=10)
N = st.sidebar.slider("Número de Pasos de Tiempo", min_value=100, max_value=1000, value=500, step=50)
a = st.sidebar.slider("Punto final (a) en t=1", min_value=-3.0, max_value=3.0, value=0.0, step=0.1)

st.sidebar.button("Generar Nuevas Rutas")

T = 1.0
dt = T / (N - 1)
t = np.linspace(0, T, N)

dW = np.sqrt(dt) * np.random.randn(M, N - 1)
W = np.zeros((M, N))
W[:, 1:] = np.cumsum(dW, axis=1)

B = W - (t / T) * (W[:, -1:] - a)

varianza_empirica = np.var(B, axis=0)
varianza_teorica = t * (1 - t)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

for i in range(min(100, M)):
    ax1.plot(t, B[i], alpha=0.3, color='#0369a1')
    
ax1.axhline(a, color='red', linestyle='--', linewidth=2, label=f'Destino final a = {a}')
ax1.set_title('Trayectorias de Puentes Brownianos')
ax1.set_xlabel('Tiempo (t)')
ax1.set_ylabel('Valor B(t)')
ax1.grid(True, alpha=0.3)
ax1.legend()

ax2.plot(t, varianza_empirica, label='Varianza Empírica', color='#0ea5e9', linewidth=2)
ax2.plot(t, varianza_teorica, label='Varianza Teórica t(1-t)', color='black', linestyle='dashed', linewidth=2)
ax2.axvline(0.5, color='green', linestyle=':', linewidth=2, label='Máximo Teórico en t=0.5')
ax2.set_title('Verificación de la Varianza')
ax2.set_xlabel('Tiempo (t)')
ax2.set_ylabel('Varianza')
ax2.grid(True, alpha=0.3)
ax2.legend()

st.pyplot(fig)