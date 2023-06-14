import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("MeanMaker")
uploaded_file = st.file_uploader("Indique el CSV que desea analizar", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))

    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    column = st.selectbox("Seleccione una columna", numeric_columns)

    if st.button('Graficar'):
        # Calculate the mean of the selected column
        mean = df[column].mean()

        # Create a plot
        fig, ax = plt.subplots()
        ax.hist(df[column], bins=30, alpha=0.5, color='g')
        ax.axvline(mean, color='r', linestyle='dashed', linewidth=2)
        ax.set_xlabel(column)
        ax.set_ylabel('Frecuencia')
        ax.set_title(f'Distribución de {column} con Mean')

        # Display the plot
        st.pyplot(fig)
