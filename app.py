import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('dark_background')

def main():
    st.title("Exploratory Data Analysis (EDA) App")

    # Sidebar section for file download and EDA options
    st.sidebar.header("Data Options")

    # Upload a dataset
    uploaded_file = st.sidebar.file_uploader("Upload a dataset (CSV)")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)

        # Show a sample of the data
        st.subheader("Sample of the dataset:")
        st.dataframe(data.head())

        # EDA options
        st.sidebar.header("Exploratory Data Analysis")
        numerical_columns = data.select_dtypes(include=[np.number]).columns.tolist()
        categorical_columns = data.select_dtypes(include=[object]).columns.tolist()

        # Select columns for EDA
        numerical_column = st.sidebar.selectbox("Select a numerical column for analysis", numerical_columns)
        categorical_column = st.sidebar.selectbox("Select a categorical column for analysis", categorical_columns)

        # Display EDA charts
        st.subheader("Exploratory Data Analysis")
        if st.sidebar.checkbox("Show summary statistics"):
            st.write("Summary Statistics:")
            st.write(data.describe())

        if st.sidebar.checkbox("Show Pairplot"):
            st.write("Pair plot:")
            st.pyplot(sns.pairplot(data, hue = categorical_column))
            #st.write(corr_matrix)

        if st.sidebar.checkbox("Show distribution of numerical data"):
            st.write(f"Distribution of {numerical_column}:")
            st.pyplot(plot_histogram(data[numerical_column]))

        if st.sidebar.checkbox("Show count plot of categorical data"):
            st.write(f"Count Plot of {categorical_column}:")
            st.pyplot(plot_countplot(data[categorical_column]))

def plot_histogram(data):
    plt.figure(figsize=(8, 6))
    sns.histplot(data, kde=True)
    plt.xlabel("Values")
    plt.ylabel("Frequency")
    return plt

def plot_countplot(data):
    plt.figure(figsize=(8, 6))
    print(type(data))
    sns.countplot(x = data)
    plt.xticks(rotation=45)
    plt.xlabel("Categories")
    plt.ylabel("Count")
    return plt

if __name__ == "__main__":
    main()
