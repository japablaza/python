import streamlit as st

# Display Code

def nombre():
    return "Pepe"

with st.echo():
    def simbolos():
        return "!@#$%^&*()"

    saludo = "Hola, soy "
    user   = nombre()
    sim    = simbolos()

    st.write(saludo, user, sim)

lol = 'jajaj'
st.write("Listo")

# Divider
st.divider()
st.title("Hola mundo")
st.divider()