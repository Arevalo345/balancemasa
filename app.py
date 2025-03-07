
import streamlit as st

# Título de la aplicación
st.title("Cálculo de cantidad de azúcar y agua para la producción de néctar")

# Descripción
st.write("""
Este programa te permite calcular la cantidad de azúcar y agua que debes agregar a la pulpa para producir el néctar con un Brix específico.
""")

# Entradas de datos
pulpa_kg = st.number_input("Ingrese la cantidad de pulpa (kg):", min_value=0.0, value=660.0)
brix_pulpa = st.number_input("Ingrese el Brix de la pulpa:", min_value=0.0, value=7.0)
nectar_kg = st.number_input("Ingrese la cantidad de néctar deseado (kg):", min_value=0.0, value=800.0)
brix_nectar = st.number_input("Ingrese el Brix del néctar deseado:", min_value=0.0, value=12.0)

# Cálculos
solidos_pulpa_kg = (brix_pulpa / 100) * pulpa_kg
solidos_nectar_kg = (brix_nectar / 100) * nectar_kg
azucar_kg = solidos_nectar_kg - solidos_pulpa_kg
agua_kg = nectar_kg - pulpa_kg - azucar_kg

# Mostrar los resultados
if st.button("Calcular"):
    st.write(f"**Cantidad de azúcar a agregar:** {azucar_kg:.2f} kg")
    st.write(f"**Cantidad de agua a agregar:** {agua_kg:.2f} kg")