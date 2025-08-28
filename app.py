import streamlit as st

def celsius_a_fahrenheit(celsius):
    """
    Función que convierte una temperatura de Celsius a Fahrenheit.
    La fórmula de conversión es: (Celsius * 9/5) + 32.
    """
    return (celsius * 9/5) + 32

# Configuración de la página
st.set_page_config(
    page_title="Conversor de Temperatura",
    page_icon="🌡️",
    layout="centered"
)

# Título de la aplicación
st.title("🌡️ Conversor de Celsius a Fahrenheit")

# Descripción de la aplicación
st.markdown("""
Esta es una sencilla aplicación web construida con Streamlit para transformar
una temperatura de grados Celsius a grados Fahrenheit.
""")

# Componente de entrada para el usuario
st.subheader("Introduce la temperatura en grados Celsius:")
celsius = st.number_input("Grados Celsius", value=0.0, step=1.0)

# Realizar la conversión
fahrenheit = celsius_a_fahrenheit(celsius)

# Mostrar el resultado al usuario con formato
st.success(f"**Resultado:** {celsius:.2f}°C equivalen a {fahrenheit:.2f}°F")

st.divider()

# Sección adicional para más información
st.info("💡 Consejo: Esta aplicación es completamente interactiva. El resultado se actualizará al instante cada vez que cambies el valor de los grados Celsius.")


