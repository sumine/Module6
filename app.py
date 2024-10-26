import pandas as pd
import streamlit as st
import plotly_express as px


st.title("Module 6 Project")

# Leer el csv con la base de datos
car_data = pd.read_csv("vehicles_us.csv")

#Muestra el dataframe. El checkbox filtra el dataframe por los carros listados 
#durante más de 100 días.
st.header("Vehicles Dataframe")
automatic = st.checkbox("Show only those listed for more than 100 days")
if automatic:
  st.dataframe(car_data[car_data["days_listed"] > 100])
else:
  st.dataframe(car_data)

#Gráfica de dispersión que solo se muestra si se selecciona el checkbox
st.header("Scatter plot odometer vs price")
odometer_graph = st.checkbox("Make a scatter plot")
if odometer_graph:
  st.write("We are making a scatter plot!")
  fig = px.scatter(car_data, x="odometer", y="price",
                   labels=dict(odometer="Odometer", price="Price ($)"))
  st.plotly_chart(fig)

#Histograma que compara el precio de dos modelos. Los modelos se seleccionan.
st.header("Comparison of price between two models")
model_1 = st.selectbox("Select the first model",
                       (car_data["model"].unique()))
model_2 = st.selectbox("Select the second model",
                       (car_data["model"].unique()),index=3)
fig = px.histogram(car_data[(car_data["model"] == model_1) | (car_data["model"] == model_2)],
                   x="price", color="model", labels=dict(price="Price ($)", model="Model"))
st.plotly_chart(fig)

st.header("Histogram of condition vs model year")
fig = px.histogram(car_data, x="model_year", color="condition",
                   labels=dict(model_year="Model year", condition="Condition"))
st.plotly_chart(fig)

