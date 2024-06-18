import streamlit as st

# Session state
if "counter" not in st.session_state:
    st.session_state.counter = 0
    
st.session_state.counter += 1

st.header(f"El sitio ha cargado {st.session_state.counter} veces")
st.button("Reinicia el sitio")