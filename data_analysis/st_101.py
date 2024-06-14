import streamlit as st
import pandas as pd
import numpy as np

#Widgets
a = st.slider('Temperatura')
st.write(a, 'cuadrado', a * a)

#Widget and session
st.text_input("Cual es tu nombre? ", key="nombre")
st.session_state.nombre

data = pd.read_csv('estat_tps00203_en.csv')

#Show/hide data
if st.checkbox("Muestra el dataframe"):
    data
    
if st.checkbox('Muestra el texto'):
    st.write('Hola Mundo!')

#Selectbox
selecciona = st.selectbox(
    "Que objeto quiere llevar? ",
    ["auto","casa","perro"]
)

"tu quieres el: ", selecciona
# data #Display dataframe using Magic
st.write("First Table with Pandas")
st.write(data)

# st.write("First Table")
# st.table(data)

st.write("First dataframe")
st.dataframe(data)

# Nice way to highlight information
df = pd.DataFrame(np.random.randn(10,20),
                  columns=('COL %d' % i for i in range(20)))

st.table(df.style.highlight_max(axis=0))

# Insert a chart
st.line_chart(df)

# Insert a Map

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [12,11] + [-33.86, 151.2],
    columns=['lat', 'lon']
)

st.map(map_data)