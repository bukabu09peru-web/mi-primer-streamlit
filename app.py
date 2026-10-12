import streamlit as st

st.title("Mi primera aplicación")

nombre = st.text_input("¿Cuál es tu nombre?")

if nombre:
    st.success(f"Hola {nombre}, bienvenido")
