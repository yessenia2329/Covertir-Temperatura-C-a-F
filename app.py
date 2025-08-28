# main.py

import streamlit as st

def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de Celsius a Fahrenheit.
    La fórmula es F = (C * 9/5) + 32.
    """
    return (celsius * 9/5) + 32

st.set_page_config(
    page_title="Conversor de Temperatura",
    page_icon="🌡️"
)

st.title("🌡️ Conversor de Celsius a Fahrenheit")
st.markdown("""
Esta es una sencilla aplicación web para transformar temperaturas.
""")

# Input del usuario
try:
    celsius_input = st.number_input("Introduce la temperatura en grados Celsius:", format="%.2f")
    
    if celsius_input is not None:
        fahrenheit_output = celsius_a_fahrenheit(celsius_input)
        st.success(f"**{celsius_input}°C** equivalen a **{fahrenheit_output:.2f}°F**")
        
except Exception as e:
    st.error(f"Ocurrió un error: {e}")

st.divider()

st.info("💡 Consejo: Puedes usar esta herramienta para convertir cualquier valor de temperatura.")
