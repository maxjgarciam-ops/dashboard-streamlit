import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import requests

url = "https://prestadoreschile-my.sharepoint.com/:u:/g/personal/m_garcia_help_cl/EdXIvaeRcwZIo8OYWgg0tKUBOGhR9UZkv5YM4uEL91E4nA?e=63WPQf"
response = requests.get(url)
df = pickle.loads(response.content)

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
