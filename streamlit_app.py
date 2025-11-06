import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import requests

url = "https://github.com/maxjgarciam-ops/dashboard-streamlit/raw/refs/heads/main/Data/Cob_202510_Telecobro_FutM_ConDesct..pkl"
response = requests.get(url)
df = pickle.loads(response.content)
st.write("Columnas disponibles:", df.columns.tolist())


# Título
st.title("Panel de Reportes Semanales")

# Filtros
st.sidebar.header("Filtros")
opciones = st.sidebar.multiselect("Selecciona categorías", df["categoria"].unique())

# Filtrado
if opciones:
    df = df[df["categoria"].isin(opciones)]

# Gráfico
st.subheader("Gráfico de barras")
fig, ax = plt.subplots()
df.groupby("categoria")["valor"].sum().plot(kind="bar", ax=ax)
st.pyplot(fig)

# Tabla
st.subheader("Datos filtrados")
st.dataframe(df)
