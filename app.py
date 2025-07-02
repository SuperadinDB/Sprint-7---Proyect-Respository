import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us_cleaned.csv')

st.header("Proyecto Sprint 7")
st.subheader("Implementación de una aplicación web con Streamlit")
st.write("Esta aplicación, realiza un análisis exploratorio de datos del dataset \
         'vehicles_us_cleaned.csv', que es el dataframe 'vehicles_us', \
         ya procesado y con el formato adecuado para su visualización.")

show_hist_button = st.checkbox("Construir histograma")

if show_hist_button:
    st.write("Este histograma muestra la distribución de los precios de los vehículos en el dataset.")
    fig = px.histogram(df, x="price", nbins=50, title="Distribución de precios de vehículos")
    st.plotly_chart(fig)

show_scatter_button = st.checkbox("Construir gráfico de dispersión")

if show_scatter_button:
    st.write("Este gráfico de dispersión muestra la relación entre el año del modelo y el precio de los vehículos.")
    fig = px.scatter(df, x="model_year", y="price", title="Relación entre año del modelo y precio")
    st.plotly_chart(fig)



