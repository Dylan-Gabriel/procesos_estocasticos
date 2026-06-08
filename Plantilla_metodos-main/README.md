# 📐 Plantilla — Métodos Numéricos II

> **FES Acatlán · UNAM**  
> Plantilla base en Streamlit para proyectos de la materia de Métodos Numéricos II.

---

## 📋 Descripción

Esta plantilla sirve como punto de partida para el proyecto final de Métodos Numéricos II. Incluye la estructura de páginas de Streamlit, la portada institucional de la FES Acatlán/UNAM, y algunos métodos numéricos ya implementados con graficación interactiva mediante Plotly.

Los métodos faltantes (BFGS, Integración, Derivación) están pendientes de completarse. También puedes agregar tus propios métodos o modificar cualquier parte del código.

---

## 🗂️ Estructura del proyecto

```
Plantilla_metodos-main/
│
├── Main.py              # Página principal: portada institucional (UNAM / FES Acatlán)
├── pages/               # Carpeta con las páginas de cada método numérico
│   └── ...              # Cada archivo .py en esta carpeta es una página de Streamlit
├── Im1.png              # Imagen del escudo de la UNAM (usada en la portada)
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Este archivo
```

---

## ⚙️ Instalación y ejecución

### 1. Clona el repositorio

```bash
git clone https://github.com/Dylan-Gabriel/procesos_estocasticos.git
cd procesos_estocasticos/Plantilla_metodos-main
```

### 2. (Recomendado) Crea un entorno virtual

```bash
python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows
```

### 3. Instala las dependencias

```bash
pip install streamlit
pip install -r requirements.txt
```

### 4. Ejecuta la aplicación

```bash
streamlit run Main.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`.

---

## 📦 Dependencias

| Librería | Versión | Uso |
|---|---|---|
| `streamlit` | latest | Framework de la aplicación web |
| `sympy` | 1.11.1 | Cálculo simbólico (derivadas, ecuaciones, etc.) |
| `matplotlib` | 3.7.0 | Graficación 2D/3D estática |
| `matplotlib-inline` | 0.1.6 | Renderizado de figuras en Streamlit |
| `plotly` | 5.14.1 | Graficación interactiva 2D y 3D |
| `numpy` | (incluido con streamlit) | Operaciones numéricas |
| `pandas` | (incluido con streamlit) | Manejo de datos tabulares |

---

## 📊 Graficación con Plotly

### Gráficas en 2D

```python
import plotly.graph_objects as gro

plo = gro.Figure()
plo.add_trace(gro.Scatter(x=valores_x, y=valores_y, mode='lines', name='f(x)'))
st.plotly_chart(plo)
```

### Gráficas en 3D

```python
import plotly.graph_objects as gro
import numpy as np

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

plo = gro.Figure()
plo.add_trace(gro.Surface(z=Z, x=X, y=Y))
st.plotly_chart(plo)
```

---

## 🧮 Cálculo simbólico con SymPy

```python
import sympy as sy

x = sy.Symbol('x')
f = sy.sin(x) * sy.exp(-x)
df = sy.diff(f, x)

st.latex(sy.latex(df))
```

---

## 🗺️ Cómo agregar un método nuevo

1. Crea un archivo `.py` dentro de `pages/`, por ejemplo `pages/3_Derivacion.py`.
2. Streamlit lo detecta automáticamente y lo agrega al menú lateral.
3. Estructura sugerida:

```python
import streamlit as st
import sympy as sy
import numpy as np
import plotly.graph_objects as gro

st.title("Nombre del Método")
st.markdown("Descripción breve del método.")

expr_input = st.text_input("Ingresa f(x):", "x**2 - 4")

x = sy.Symbol('x')
f = sy.sympify(expr_input)

# ... implementación del método ...

plo = gro.Figure()
# ... construye la gráfica ...
st.plotly_chart(plo)
```

---

## ✅ Estado de los métodos

| Método | Estado |
|---|---|
| Portada institucional | ✅ Implementado |
| BFGS | ⬜ Pendiente |
| Integración numérica | ⬜ Pendiente |
| Derivación numérica | ⬜ Pendiente |

---

**Profesor:** Julio César Galindo López  
**Materia:** Métodos Numéricos II  
**Facultad:** Facultad de Estudios Superiores Acatlán — UNAM

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](./LICENSE) para más detalles.
