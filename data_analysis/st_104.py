import streamlit as st
import pandas as pd
import numpy as np

if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20,2), columns=["x","y"])
    
st.header("Selecciona un color")
color = st.color_picker("color", "#FF1234")
st.divider()
st.scatter_chart(st.session_state.df, x="x", y="y", color=color)