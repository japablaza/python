import streamlit as st
import time

# Panel a la derecha
caja_selectora = st.sidebar.selectbox(
    "Metodos de contacto",
    ["Telefono", "Email", "Directo"]
)

slider_uno = st.sidebar.slider(
    "Selecciona un valor",
    0.0, 90.0, (25.0, 75.0)
)

# Columnas

izq, der = st.columns(2)

izq.button("Apreta")

der.radio(
    "Que color usas? ",
    ["rojo","verde","azul"]
)

with der:
    seleccion = st.radio(
        "A donde Quieres ir de vacaciones? ",
        ['Peru', "Argentina", "Chile"]
    )
    f"Queres ir a {seleccion}!!, que buena eleccion"
    
barra = izq.progress(0)
# barra
for a in range(100):
    barra.progress(a + 1)
    time.sleep(0.1)