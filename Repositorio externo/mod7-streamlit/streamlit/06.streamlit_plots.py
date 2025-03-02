import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def main():

    st.title("Plots")

    with st.expander(label = "DataFrame - Tips", expanded = False):
        df = sns.load_dataset(name = "tips")
        st.dataframe(df)

    # plt.scatter(x = df["total_bill"], y = df["tip"])
    # st.pyplot()

    fig, ax = plt.subplots()
    ax.scatter(x = df["total_bill"], y = df["tip"])
    plt.title("Total Bill vs Tip")
    plt.xlabel("Total Bill")
    plt.ylabel("Tip")
    st.pyplot(fig)


    fig = plt.figure()
    sns.countplot(x = df["sex"])
    st.pyplot(fig)

    fig = plt.figure()
    sns.scatterplot(x = df["total_bill"], y = df["tip"],
                    hue = df["smoker"], alpha = 0.5)
    st.pyplot(fig) 


    fig = plt.figure()
    sns.boxplot(x = df["day"], y = df["tip"], hue = df["smoker"])
    st.pyplot(fig) 


    fig, ax = plt.subplots(nrows = 2, ncols = 2)
    sns.histplot(x = df["total_bill"], kde = True, ax = ax[0, 0]);
    sns.countplot(x = df["size"], ax = ax[0, 1]);
    sns.scatterplot(x = df["tip"], y = df["size"], hue = df["smoker"], ax = ax[1, 0]);
    sns.boxplot(x = df["time"], y = df["total_bill"], ax = ax[1, 1]);
    st.pyplot(fig)
    
    fig = plt.figure()
    sns.kdeplot(df, x='tip')
    sns.rugplot(df, x='tip')
    st.pyplot(fig)
    
    x = np.linspace(0, 10, 100)

    fig = plt.figure(figsize=(10, 6))  # Definir el tamaño de la figura

    # Primer subplot (fila 1, columna 1)
    plt.subplot(2, 2, 1)  # (filas, columnas, índice)
    plt.plot(x, np.sin(x), label="Seno", color="b")
    plt.title("Seno")
    plt.legend()

    # Segundo subplot (fila 1, columna 2)
    plt.subplot(2, 2, 2)
    plt.plot(x, np.cos(x), label="Coseno", color="r")
    plt.title("Coseno")
    plt.legend()

    # Tercer subplot (fila 2, columna 1)
    plt.subplot(2, 2, 3)
    plt.plot(x, np.tan(x), label="Tangente", color="g")
    plt.title("Tangente")
    plt.ylim(-5, 5)  # Limitar eje Y para evitar valores extremos
    plt.legend()

    # Cuarto subplot (fila 2, columna 2)
    plt.subplot(2, 2, 4)
    plt.plot(x, np.exp(-x), label="Exponencial", color="m")
    plt.title("Exponencial")
    plt.legend()
    st.pyplot(fig)
    

    pass

if __name__ == "__main__":
    main()